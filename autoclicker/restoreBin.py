# =============================================================================
#   Filename         : resotoreBin.py
#
#   Created On       : 2021-10-13 20:34
#
#   Last Modified    :
#
#   Revision         : 1.0
#
#   Author           : HuangYeshun
#
#   Description      : Introduce the use of autoclicker and try to use it for my onedrive recycle bin restore
'''


'''
# =============================================================================


from pymouse import PyMouse
import time
# point 1 select all
pos_sel=[214,315]
# point 2 restore
pos_retr=[213,270]
# point 3 confirm
pos_cfm=[838,165]

m=PyMouse()


while (True):
    pos_now= m.position()               # record pose
    print(pos_now)
    m.click(pos_sel[0],pos_sel[1],1,1)   # move position
    time.sleep(0.1)
    m.click(pos_retr[0],pos_retr[1],1,1) # move position
    time.sleep(0.5)
    m.click(pos_cfm[0],pos_cfm[1],1,1)   # move position
    m.move(pos_now[0],pos_now[1])   # get back to the original
    # m.click()
    time.sleep(10)

# while (True):
#     a = m.position() # get position
#     time.sleep(2)
#     print(a)