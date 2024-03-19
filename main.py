import tornado.ioloop
from handler.not_found_handler import NotFoundHandler
from handler.user.options import UserOptionsHandler
from handler.user.forms import UserFormsHandler
from handler.user.form.questions import UserFormQuestionsHandler
from handler.user.form.question.answers import UserFormQuestionAnswersHandler
from handler.user.questions import UserQuestionsHandler
from handler.user.question.answers import UserQuestionAnswersHandler
from handler.user.dashboards import UserDashboardsHandler
from handler.user.dashboard.dashboard import UserDashboardHandler
from handler.user.dashboard.default import UserDashboardDefaultHandler
from handler.user.default import UserDefaultHandler

def make_app():
    return tornado.web.Application([
        (r"/options", UserOptionsHandler),
        (r"/forms", UserFormsHandler),
        (r"/form/([^/]+)/questions", UserFormQuestionsHandler),
        (r"/form/([^/]+)/question/([^/]+)/answers", UserFormQuestionAnswersHandler),
        (r"/questions", UserQuestionsHandler),
        (r"/question/([^/]+)/answers", UserQuestionAnswersHandler),
        (r"/dashboards", UserDashboardsHandler),
        (r"/dashboard/([^/]+)", UserDashboardHandler),
        (r"/dashboard/([^/]+)/default", UserDashboardDefaultHandler),
        (r"/default", UserDefaultHandler),
    ], default_handler_class=NotFoundHandler)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # Il server ascolta sulla porta 8888
    tornado.ioloop.IOLoop.current().start()