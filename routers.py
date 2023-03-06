'''obsolete'''

# class ToDoDBRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'ToDo':
#             return 'mongo'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'ToDo':
#             return 'mongo'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label == 'ToDo' or obj2._meta.app_label == 'ToDo':
#             return True
#         return None
