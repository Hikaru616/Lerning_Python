class Registry:
    registries = []
    
    def __init__(self, name='ABC'):
        print('コンストラクタ呼び出し')
        self.name = name
        Registry.registries.append(self.name)
        
    def __del__(self):
        print(f"{self.name}を削除")
        Registry.registries.remove(self.name)
        # __del__(特殊メソッドの一つ)
        # __del__をクラスないに設定しておくことで、最終的にメモリ解放時に呼び出される
        # 設定していない時は、別の方法でメモリ解放される
        # __del__を設定しておくことで、最終的に自動で呼び出される → print内処理も呼び出される
        
    def print_name(self):
        print(self.name)
        
a = Registry('A')
b = Registry('B')
c = Registry()

a.print_name()
b.print_name()
c.print_name()
print(Registry.registries)

del a
print('プログラムが終了しました')
