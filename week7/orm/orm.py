# # # import psycopg2 

# # # connection = psycopg2.connect(
# # #     database = 'orm_db',
# # #     user = 'aika',
# # #     password = '1',
# # #     # host = 'localhost',
# # #     # port = '5432'
# # # )
# # # print('Database orm_db opened')

# # # cursor = connection.cursor() #cursor is used for the execution of our commands in database
# # #                             #execute lets as to call methods
# # # # cursor.execute(
# # # #     '''CREATE TABLE company(
# # # #         id SERIAL PRIMARY KEY,
# # # #         name varchar(50) NOT NULL,
# # # #         city VARCHAR(50) NOT NULL
# # # #     )
# # # #     '''
# # # # ) need to comment the execute so that it does not create one more table 
# # # # print('Table successfully created')
# # # # connection.commit() # create changes in our database
# # # # connection.close()

# # # # cursor.execute()

# # # cursor = connection.cursor() #cursor is used for the execution of our commands in database
# # # # cursor.execute(
# # # #     '''INSERT INTO company(name, city) VALUES ('IBM', 'Los Angeles'), 
# # # #     ('Apple', 'Cupertino'), ('HP', 'New York'), ('Dell', 'New Jersey')
# # # #     '''
# # # # )
# # # # connection.commit()
# # # # print('Inserted successfully')
# # # # connection.close()
# # # # cursor.execute(
# # # #     '''INSERT INTO company(name, city) values ('Samsung', 'Seoul')
# # # #     '''
# # # # )
# # # # cursor.execute(
# # # #     '''INSERT INTO company(name, city) values ('Toyota', 'Tokio')
# # # #     '''
# # # # )
# # # # connection.commit()
# # # # connection.close()

# # # # cursor = connection.cursor()
# # # # cursor.execute(
# # # #     '''
# # # #     SELECT * FROM company
# # # #     '''
# # # # )
# # # # data = cursor.fetchall()
# # # # for item in data:
# # # #         print(f'id: {item[0]}, name: {item[1]}, city: {item[2]}')
# # # #         print(*item)
# # # # connection.close() 


# # # #######################
# # # # cursor.execute(
# # # #     '''
# # # #     SELECT name, city FROM company WHERE id=2
# # # #     '''
# # # # )
# # # # data = cursor.fetchone()
# # # # print(data)

# # # ###############
# # # # cursor = connection.cursor()
# # # # cursor.execute(
# # # #     '''
# # # #     UPDATE company SET city = 'New Mexico' WHERE id=2
# # # #     '''
# # # # )
# # # # connection.commit()
# # # # cursor.execute(
# # # #     '''
# # # #     SELECT * FROM company order by id
# # # #     '''
# # # # )
# # # # data = cursor.fetchall()
# # # # for item in data:
# # # #     print(*item)
# # # # connection.close()
# # # ###################
# # # cursor = connection.cursor()
# # # cursor.execute(
# # #     '''
# # #     DELETE FROM company WHERE id in (3, 6)
# # #     '''
# # # )
# # # connection.commit()
# # # print(f'Total count of deleted rows: {cursor.rowcount}')
# # # cursor.execute(
# # #     '''SELECT * FROM company order by id
# # #     '''
# # # )
# # # data = cursor.fetchall()
# # # for item in data:
# # #     print(*item)
# # # connection.close()
# # ###################################
# # ###################### SQL ALCHEMY ############################

# # # from sqlalchemy import create_engine
# # # engine = create_engine('postgresql+psycopg2://aika: @localhost:5432/orm_db') #after aika (username) should a password if there is one
# # # print('Database connected')

# # # from sqlalchemy import Column, Table, Integer, String, MetaData

# # # metadata = MetaData() #collection of object in the table and its child objects are called metadata
# # # students_table = Table(
# # #     'students', metadata,
# # #     Column('id', Integer, primary_key = True),
# # #     Column('name', String),
# # #     Column('last_name', String)
# # # )
# # # students_table.create(bind = engine) #creating the table
# # # print('Successfully created the table')

# # # inserted_data = students_table.insert().values(name = 'John', last_name = 'Snow')
# # # inserted_data = students_table.insert().values(name = 'Alice', last_name = 'Clark')
# # # engine.execute(inserted_data)
# # # print('Successfully inserted')
# # #######################
# # # from sqlalchemy import select
# # # query = select([students_table.c.name, students_table.c.last_name])
# # # name, last_name = engine.execute(query).fetchone() #John Snow
# # # print(name, last_name)

# # # ################################
# # # from sqlalchemy import select
# # # query = select([students_table.c.name, students_table.c.last_name])
# # # data = engine.execute(query).fetchall() #John Snow
# # # for item in data:
# # #     print(*item)
# # # #John Snow
# # # # Alice Clark
# # # ###############################
# # ################using mapping##############
# # # from sqlalchemy import create_engine
# # # engine = create_engine('postgresql+psycopg2://aika: @localhost:5432/orm_db') #after aika (username) should a password if there is one
# # # from sqlalchemy import Column, Table, Integer, String, MetaData
# # # metadata = MetaData() #collection of object in the table and its child objects are called metadata
# # # company_table = Table(
# # #     'company', metadata,
# # #     Column('id', Integer, primary_key = True),
# # #     Column('name', String),
# # #     Column('city', String)
# # # )
# # # metadata.create_all(engine)
# # # class Company:
# # #     def __init__(self, name, city):
# # #         self.name = name
# # #         self.city = city
# # #     def __str__(self):
# # #         return f'Company {self.name}, City {self.city}'
# # # from sqlalchemy.orm import mapper
# # # mapper(Company, company_table)
# # # print('Successfully created table')

# # ###################### EASIER WAY TO CREATE A TABLE, without metadata, mapper##################

# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('postgresql+psycopg2://aika: @localhost:5432/orm_db') #after aika (username) should a password if there is one
# Base = declarative_base() #lets us to create classes, takes the role of the Parent of all classes
# class Company(Base):
#     __tablename__ = 'company'
#     id = Column(Integer, primary_key = True)
#     name = Column(String)
#     city = Column(String)
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city
#     def __str__(self):
#         return f'Company {self.name}, City {self.city}'
# # # Base.metadata.create_all(engine)
# # # print('Table Created')

# # #before we insert some value into the table, 
# # # we must create a Session
# # # Session maker takes the role of a cursor, so that we stay connected to the database



# # ############## ADDING DATA to the table using SESSION#############
# Session = sessionmaker(bind=engine)
# session = Session()
# # apple = Company('Apple', 'Cupertino')
# # # session.add(apple)
# # # session.commit()
# # ############# EXPORTING DATA FROM the table#########
# # # query = session.query(Company.name, Company.city).all()
# # # for item in query:
# # #     print(*item)
# # ####################################################
# # # samsung = Company('Samsung', 'Seoul')
# # # session.add(samsung)
# # # session.commit()
# # # query = session.query(Company.name, Company.city).first() #returns only the first value
# # # print(query)
# # ###################################################
# # ################### CHOOSING THE DATA (WHEN)#########
# # # our_company = session.query(Company).filter_by(city = 'Seoul').first()
# # # '''
# # # same as SELECT * FROM company WHERE city = 'Seoul'
# # # '''
# # # print(our_company) ##HERE OUR __str__ function is executed
# # ############## INSERTING MANY ROWS ############
# # # session.add_all([Company('IBM', 'Washington'), Company('Dell', 'New York')])
# # # session.commit()
# # # query = session.query(Company.name, Company.city).all()
# # # for item in query:
# # #     print(*item)
# # #################################################

# # # query = session.query(Company.name, Company.city).order_by('city').all()
# # # for item in query:
# # #     print(*item)

# ##########################
# # query = session.query(Company.name, Company.city).order_by('city').all()
#      #SELECT name, city from company order by id;
# # for item in query:
# #     print(*item)

# # #########################6#####################
# # session.add_all([Company('IBM', 'Washington'), Company('Dell', 'New York')])
# # session.commit()
# # query = session.query(Company.name, Company.city).order_by('city').first() #-->fetchall
# # print(*query)
# # # for item in query:
# # #     print(*item)

# # from datetime import datetime
# # s = datetime.now()
# # import functools
# # list_ = [num for num in range(10000, 100000) if num%2 ==0]
# # for num in list_:
# #     if str(num)[2] in ('1', '3', '5', '7', '9'):
# #         a=list(str(num))
# #         a=[int(i) for i in a ]
# #         sum_ = sum(a)
# #         if sum_%4 == 0:
# #             print(num)
# #     else:
# #         pass
# # e = datetime.now()
# # print(e-s)
# ##############################################


