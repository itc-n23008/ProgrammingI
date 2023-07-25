def show_begin_end(func):
       呼ばれた関数の始めと終わりを表示するデコレータ
    def deco_func(*args, **kwargs):
           関数を実行する前を後にメッセージを表示
        print('== stsrt')
        result = func(*args, **kwargs)
        print('== end')
        return result
    return deco_func
