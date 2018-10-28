# -*- coding:utf-8 -*-
__date__ = '2018/10/28 14:44'

class Field:
    pass

class IntField(Field):
    def __init__(self, db_column=None, min_value=None, max_value=None):
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value
        self._value = None

    def __set__(self, instance, value):
        self._value = value

    def __get__(self, instance, value):
        return self._value

    def __delete__(self, instance):
        pass

class CharField(Field):
    def __init__(self, db_column=None, max_length=None):
        self.db_column = db_column
        self.max_length = max_length
        self._value = None

    def __set__(self, instance, value):
        self._value = value

    def __get__(self, instance, value):
        return self._value

    def __delete__(self, instance):
        pass

class ModleMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        print("ModleMetaClass new ", name)
        if name == "BaseModle":
            return super().__new__(cls, name, bases, attrs, **kwargs)

        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table

        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)

    def __init__(self, name, bases, attrs, **kwargs):
        print("ModleMetaClass init", name)

class BaseModle(metaclass=ModleMetaClass):
    def __init__(self, *args, **kwargs):
        print("base init")
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def sava(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))

        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta["db_table"], fields=",".join(fields), values=",".join(values))
        print(sql)

class User(BaseModle):
    # def __init__(self, name, age):
    #     print("user init")
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=1, max_value=100)

    class Meta:
        db_table = "user"

if __name__ == "__main__":
    u = User(name="xiaoming", age=28)
    u.sava()

# 输出：
# ModleMetaClass new  BaseModle
# ModleMetaClass init BaseModle
# ModleMetaClass new  User
# ModleMetaClass init User
# base init
# insert user(name,age) value(xiaoming,28)