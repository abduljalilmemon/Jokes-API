from environs import Env

env = Env()
WORKER_ENV = env('WORKER_ENV', 'local')

if WORKER_ENV == 'local':
    env.read_env()

DATABASE_URL = env.str('DATABASE_URL')
JWT_SECRET = env.str('JWT_SECRET')
JWT_ALGORITHM = env.str('JWT_ALGORITHM')
USERS = env.json('USERS', {})
QUOTA = env.int('QUOTA', 5)
