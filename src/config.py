from environs import Env

env = Env()
WORKER_ENV = env('WORKER_ENV', 'local')

if WORKER_ENV == 'local':
    env.read_env()

DATABASE_URL = env.str('DATABASE_URL')
