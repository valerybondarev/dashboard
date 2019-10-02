from peewee import *
import datetime


db_user = ''
db_password = ''
db_name = ''
db_host = 'localhost'
db_port = '5432'

pg_db = PostgresqlDatabase(db_name, user=db_user, password=db_password,
                           host=db_host, port=db_port)
now = datetime.datetime.now()

class BaseModel(Model):
    class Meta:
        database = pg_db

#
# class Issue_category(BaseModel):
#     id = PrimaryKeyField(null=False, primary_key=True)
#     title = CharField(max_length=500, null=False)
#     color = CharField(max_length=50, null=False)
#
#     created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
#     updated_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
#
#     class Meta:
#         db_table = 'Issue_category'
#         order_by = 'id', 'created_at'


# Users in progress