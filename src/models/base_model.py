class BaseModel:
  def __init__(self):
    pass

  def to_json(self):
    obj_dict = self.__dict__
    for key in list(obj_dict.keys()):
      if callable(obj_dict[key]) or key.startswith('_'):
        obj_dict.remove(key)
    return obj_dict