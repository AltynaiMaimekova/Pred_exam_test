from . import views
from . import app

# urls for posts
app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
app.add_url_rule('/customer/create', view_func=views.customer_create, methods=['GET', 'POST'], endpoint='customer_create')
app.add_url_rule('/customer/<int:customer_id>', view_func=views.customer_detail, methods=['GET'], endpoint='customer_detail')
app.add_url_rule('/customer/<int:customer_id>/delete', view_func=views.customer_delete, methods=['GET', 'POST'], endpoint='customer_delete')
app.add_url_rule('/customer/<int:customer_id>/update', view_func=views.customer_update, methods=['GET', 'POST'], endpoint='customer_update')

# urls for user

app.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'], endpoint='register')
app.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'], endpoint='login')
app.add_url_rule('/logout', view_func=views.logout, methods=['GET', 'POST'], endpoint='logout')