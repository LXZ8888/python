from sqlalchemy import create_engine
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3307'
DATABASE = 'qfplat'
USERNAME = 'root'
PASSWORD = 'qingfeng123456'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# # 创建数据库引擎
engine = create_engine(DB_URI)
#
# #创建连接
# # with engine.connect() as con:
# #     rs = con.execute('SELECT 2*3')
# #     print( rs.fetchone()) #返回的结果是一个元祖
#
# '''原生sql：创建数据库表'''
# with engine.connect() as con:
    # con.execute('drop table if exists qf_users')
    #con.execute('create table qf_users(id int primary key auto_increment,name varchar(25))')
    # # 插入两条数据到表中
    # con.execute('insert into qf_users(name) values("test1")')
    # con.execute('insert into qf_users(name) values("test2")')
    # 执行查询操作
    #results = con.execute('select * from qf_users')
    #print(results.fetchone()) #返回表中一条数据
    #print(results.all()) #返回表中所有的数据

    # # 从查找的结果中遍历
    # for result in results:
    #     print(result)

'''orm来创建表'''
from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)
class Users(Base):
    # 定义表名为users
    __tablename__ = 'users'
    # 将id设置为主键，并且默认是自增长的
    id = Column(Integer,primary_key=True)
    # name字段，字符类型，最大的长度是50个字符
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(100))

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "<User(id='%s',name='%s',fullname='%s',password='%s')>" % (self.id,self.name,self.fullname,self.password)

class TestCase(Base):
    # 定义表名为users
    __tablename__ = 'testcase'
    # 将id设置为主键，并且默认是自增长的
    id = Column(Integer,primary_key=True)
    # name字段，字符类型，最大的长度是50个字符
    casename = Column(String(50))

Base.metadata.create_all()

