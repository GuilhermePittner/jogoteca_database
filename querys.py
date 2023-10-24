import psycopg2, inspect, config


#===================#
#     USER LOGIN    #
#===================#
def users_query(nickname):
    try:
      connection = config.get_db_connection()
      with connection:
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM xuot1_studies.tb_users tu where tu.nickname = %s", (nickname,))
            res_rows = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
      connection.close()
      return res_rows

    except psycopg2.DatabaseError as error:
        raise ValueError('Error on method ' + inspect.stack()[0][3])
    


#===================#
#       GAMES       #
#===================#
def games_query():
    try:
      connection = config.get_db_connection()
      with connection:
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM xuot1_studies.tb_games")
            res_rows = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
      connection.close()

      games_arr = []
      for item in res_rows:
        games_arr.append(item)

      return games_arr

    except psycopg2.DatabaseError as error:
        raise ValueError('Error on method ' + inspect.stack()[0][3])
    
  
def insert_games(name, category, platform):
    try:
      connection = config.get_db_connection()
      with connection:
          with connection.cursor() as cursor:
            cursor.execute("INSERT INTO xuot1_studies.tb_games (name, category, platform) values (%s, %s, %s)", (name, category, platform,))
           
      connection.close()
      return True

    except psycopg2.DatabaseError as error:
        raise ValueError('Error on method ' + inspect.stack()[0][3])
    

def check_games(name):
    try:
      connection = config.get_db_connection()
      with connection:
          with connection.cursor() as cursor:
            cursor.execute("SELECT * from xuot1_studies.tb_games where name = %s", (name,))
            res_rows = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]

            status = True
            if len(res_rows) == 0:
              status = False

      connection.close()
      return status

    except psycopg2.DatabaseError as error:
        raise ValueError('Error on method ' + inspect.stack()[0][3])
    

def games_info(id):
    try:
      connection = config.get_db_connection()
      with connection:
          with connection.cursor() as cursor:
            cursor.execute("SELECT * from xuot1_studies.tb_games where id = %s", (id,))
            res_rows = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]

      connection.close()
      return res_rows

    except psycopg2.DatabaseError as error:
        raise ValueError('Error on method ' + inspect.stack()[0][3])
    

def update_games(name, category, platform, id):
    try:
      connection = config.get_db_connection()
      with connection:
          with connection.cursor() as cursor:
            cursor.execute("UPDATE xuot1_studies.tb_games set name = %s, category = %s, platform = %s WHERE id = %s", (name, category, platform, id,))
           
      connection.close()
      return True

    except psycopg2.DatabaseError as error:
        raise ValueError('Error on method ' + inspect.stack()[0][3])
    

def delete_games(id):
    try:
      connection = config.get_db_connection()
      with connection:
          with connection.cursor() as cursor:
            cursor.execute("DELETE FROM xuot1_studies.tb_games WHERE id = %s", (id,))
           
      connection.close()
      return True

    except psycopg2.DatabaseError as error:
        raise ValueError('Error on method ' + inspect.stack()[0][3])