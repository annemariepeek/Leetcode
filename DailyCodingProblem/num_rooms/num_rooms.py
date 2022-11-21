def num_rooms(a):

    a.sort()
    rooms = 0

    for i in range(0, len(a)-1):
        if a[i][1] > a[i+1][0]:
            rooms += 1
            print(a[i][1], a[i+1][0])

    return rooms
    





a = [(30, 75), (0, 50), (60, 150)]
print(num_rooms(a))
# answer = 2

a = [(30, 75), (0, 50), (60, 150), (0, 40), (80, 150)]
print(num_rooms(a))
# answer = 

#   SOLUTION
# /**
#  * @param {number[][]} intervals
#  * @return {number}
#  */
# def minMeetingRooms = function(intervals) {
#  
#   startTimes = []
#   endTimes = []
#   for i in range(0,len(intervals)):


    
#   startTimes.sort((a, b) => a - b);
#   endTimes.sort((a, b) => a - b);

#   let startPointer = 0;
#   let endPointer = 0;
#   let rooms = 0;
#   while(startPointer < intervals.length) {
#     if (startTimes[startPointer++] >= endTimes[endPointer]) {
#       ++endPointer;
#     } else {
#       ++rooms;    
#     }
#   }
#   return rooms;
# };