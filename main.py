import tornado.ioloop
from handler.main_handler import MainHandler
from handler.not_found_handler import NotFoundHandler
from handler.user.options import UserOptionsHandler
from handler.user.forms import UserFormsHandler
from handler.user.form.questions import UserFormQuestionsHandler
from handler.user.form.question.answers import UserFormQuestionAnswersHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/options", UserOptionsHandler),
        (r"/forms", UserFormsHandler),
        (r"/form/([^/]+)/questions", UserFormQuestionsHandler),
        (r"/form/([^/]+)/question/([^/]+)/answers", UserFormQuestionAnswersHandler),
    ], default_handler_class=NotFoundHandler)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # Il server ascolta sulla porta 8888
    tornado.ioloop.IOLoop.current().start()