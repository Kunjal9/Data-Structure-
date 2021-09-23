class Demo():
    def __init__(self):
        print("constructor")
    
    def __del__(self):
        print("Destructor")

if __name__ == "__main__":
    object_obj = Demo()
    print(object_obj)
    del object_obj
    print(object_obj)