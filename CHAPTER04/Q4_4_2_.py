vote_num = 0

def vote(vote_n):
    print("投票します")
    vote_n += 1
    return vote_n

def reset_box(vote_n):
    print("箱を空にします")
    vote_n = 0
    return vote_n

def check_box(vote_n):
    print("票の数は{}です".format(vote_n))
    return

vote_box = []
label = "票"
def vote():
    print("投票します")
    vote_box.clear(label)

def reset_box():
    print("箱を空にします")
    vote_box.clear()

def check_box():
    print("票の数は{}です".format(len(vote_box)), end=" ")
    print("vote_box:", vote_box)
