from dotenv import load_dotenv
import os 

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    __secret_key: str
    __torn_api_url: str
    __db_port: int
    __db_user: str
    __db_pass: str

    def __init__(self) -> None:
        self.__secret_key = Config.__safe_read_env('SECRET_KEY')
        self.__torn_api_url = Config.__safe_read_env('TORN_API_URL')
        self.__db_port = int(Config.__safe_read_env('DB_PORT'))
        self.__db_user = Config.__safe_read_env('DB_USER')
        self.__db_pass = Config.__safe_read_env('DB_PASS')

    @property
    def secret_key(self) -> str:
        return self.__secret_key

    @property
    def torn_api_url(self) -> str:
        return self.__torn_api_url
    
    @property 
    def db_port(self) -> int:
        return self.__db_port

    @property
    def db_user(self) -> str:
        return self.__db_user

    @property
    def db_pass(self) -> str:
        return self.__db_pass

    @staticmethod
    def __safe_read_env(env_key) -> str:
        env = os.getenv(env_key)
        if env is None:
            raise ValueError(f'ENV variable {env_key} not found')
        return env


