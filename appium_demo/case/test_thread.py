#coding = utf-8
import threading

class MyTest:
    def test_sum(self, a):
        print a + 1

    # threads = []
    # for i in range(3):
    #     # print i
    #     thread = threading.Thread(target=sum, args=(i,))
    #     threads.append(thread)
    #     # thread.start()
    # for t in threads:
    #     t.start()

if __name__ == "__main__":
    t = MyTest()
    t.test_sum(2)