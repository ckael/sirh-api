from mvc_flask import Router

Router.get('/','notfound#index')
Router.get('/users/all','user#getAll')
Router.post('/user/add','user#addUser')
Router.post('/upload','user#upload')