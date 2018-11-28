import redis
from redis import StrictRedis


class Config(object):
    "工程配置信息"
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    DEBUG = True

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:liuxujing@127.0.0.1:3306/python2"
    # 配置数据库的动态追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis的主机和端口
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 使用redis来保存session信息
    SESSION_TYPE = 'redis'
    # 对象session信息进行签名
    SESSION_USE_SIGNER = True
    # 存储session的redis实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 指定session的过期时间1天
    PERMANENT_SESSION_LIFETIME = 86400

# 开发模式
class developmentConfig(Config):
    DEBUG = True

class productionConfig(Config):
    DEBUG = False


config = {
    'development': developmentConfig,
    'production': productionConfig
}














































