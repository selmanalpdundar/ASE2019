from flakon import JsonBlueprint
from flask import request, jsonify, abort
from myservice.classes.quiz import Quiz, Question, Answer, NonExistingAnswerError, LostQuizError, CompletedQuizError

quizzes = JsonBlueprint('quizzes', __name__)

_LOADED_QUIZZES = {}  # list of available quizzes
_QUIZNUMBER = 0  # index of the last created quizzes


@quizzes.route("/quizzes", methods=['GET', 'POST'])
def all_quizzes():
    if 'POST' == request.method:
        return create_quiz(request)
    elif 'GET' == request.method:
        return get_all_quizzes(request)


@quizzes.route("/quizzes/loaded", methods=['GET'])
def loaded_quizzes():
    return jsonify({"loaded_quizzes": len(_LOADED_QUIZZES)})


@quizzes.route("/quiz/<id>", methods=['GET', 'DELETE'])
def single_quiz(id):
    global _LOADED_QUIZZES
    result = ""

    exists_quiz(id)

    if 'GET' == request.method:
        result = jsonify(_LOADED_QUIZZES[id].serialize())
    elif 'DELETE' == request.method:
        result = jsonify({"answered_questions": _LOADED_QUIZZES[id].currentQuestion,
                          "total_questions": len(_LOADED_QUIZZES[id].questions)})
        del _LOADED_QUIZZES[id]
    return result


@quizzes.route("/quiz/<id>/question", methods=['GET'])
def play_quiz(id):
    global _LOADED_QUIZZES
    result = ""
    try:
        exists_quiz(id)
    except NonExistingAnswerError as e:
        result = e.value

    if 'GET' == request.method:
        try:
            result = jsonify(_LOADED_QUIZZES[id].getQuestion())
        except CompletedQuizError as e:
            result = jsonify({"msg": "completed quiz"})
        except LostQuizError as e2:
            result = jsonify({"msg": str(e2)})

    return result


@quizzes.route("/quiz/<id>/question/<answer>", methods=['PUT'])
def answer_question(id, answer):
    global _LOADED_QUIZZES
    result = ""
    # TODO: check if the quiz is an existing one
    try:
        exists_quiz(id)
        quiz = _LOADED_QUIZZES[id]
    except NonExistingAnswerError as e:
        result = e.value

    if 'PUT' == request.method and not quiz.isCompleted() and not quiz.isLost():
        # TODO: Check answers and handle exceptions
        try:
            result = quiz.checkAnswer(givenAnswer=answer)
        except CompletedQuizError as e:
                if len(quiz.questions) == quiz.currentQuestion-1:
                    result = "you won 1 million clams!"
                else:
                    result = str(e)
        except LostQuizError as e2:
                result = str(e2)
        print("answer : {} ".format(answer))
        return jsonify({'msg': result})


############################################
# USEFUL FUNCTIONS BELOW (use them, don't change them)
############################################

def create_quiz(request):
    global _LOADED_QUIZZES, _QUIZNUMBER

    json_data = request.get_json()
    qs = json_data['questions']
    questions = []
    for q in qs:
        question = q['question']
        answers = []
        for a in q['answers']:
            answers.append(Answer(a['answer'], a['correct']))
        question = Question(question, answers)
        questions.append(question)

    _LOADED_QUIZZES[str(_QUIZNUMBER)] = Quiz(_QUIZNUMBER, questions)
    _QUIZNUMBER += 1

    return jsonify({'quiznumber': _QUIZNUMBER - 1})


def get_all_quizzes(request):
    global _LOADED_QUIZZES

    return jsonify(loadedquizzes=[e.serialize() for e in _LOADED_QUIZZES.values()])


def exists_quiz(id):
    if int(id) > _QUIZNUMBER:
        abort(404)  # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not (id in _LOADED_QUIZZES):
        abort(410)  # error 410: Gone, i.e. it existed but it's not there anymore
