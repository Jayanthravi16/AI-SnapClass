# from src.database.config import supabase
# import bcrypt

# def hash_pass(pwd):
#     return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

# def check_pass(pwd, hashed):
#     return bcrypt.checkpw(pwd.encode(), hashed.encode())

# def check_teacher_exists(username):
#     # Check for unique username, returns flase when username is already taken
#     response = supabase.table("teachers").select("username").eq("username", username).execute()
#     return len(response.data)>0
 
# def create_teacher(username, password, name):
#     data = {"username":username, "password":hash_pass(password), "name":name}
#     response = supabase.table("teachers").insert(data).execute()
#     return response.data

# def teacher_login(username, password):
#     response = supabase.table("teachers").select("*").eq("username", username).execute()
#     if response.data:
#         teacher = response.data[0]
#         if check_pass(password, teacher['password']):
#             return teacher
#     return None

# def get_all_students():
#     response = supabase.table("students").select("*").execute()
#     return response.data

# def create_student(new_name, face_embedding=None, voice_embedding=None):
#     data = {'name':new_name, 'face_embedding':face_embedding, "voice_embedding":voice_embedding}
#     response = supabase.table("students").insert(data).execute()
#     return response.data


from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def check_teacher_exists(username):
    # Sanitize: Remove accidental spaces and make lowercase
    clean_username = username.strip().lower()
    
    response = supabase.table("teachers").select("username").eq("username", clean_username).execute()
    return len(response.data) > 0
 
def create_teacher(username, password, name):
    # Sanitize before saving to database
    clean_username = username.strip().lower()
    clean_name = name.strip()
    
    data = {
        "username": clean_username, 
        "password": hash_pass(password), 
        "name": clean_name
    }
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    # Sanitize before querying
    clean_username = username.strip().lower()
    
    response = supabase.table("teachers").select("*").eq("username", clean_username).execute()
    if response.data:
        teacher = response.data[0]
        # Note: Do not lowercase the password, as passwords ARE case-sensitive
        if check_pass(password, teacher['password']):
            return teacher
    return None

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def create_student(new_name, face_embedding=None, voice_embedding=None):
    clean_name = new_name.strip()
    data = {'name': clean_name, 'face_embedding': face_embedding, "voice_embedding": voice_embedding}
    response = supabase.table("students").insert(data).execute()
    return response.data