
def main():
    cases = int(input())
    
    for case in range(cases):
        eye_position = list(map(int,input().split()))
        
        
        screen = [[10 for j in range(20)] for i in range(20)]
        
        # Initialize the inital row
        initial_row = [10 for percent in range(20)]
        initial_row[eye_position[1]] = 100
        
        # Set all percent values for the row the eye is on
        left_side = eye_position[1] - 1
        right_side = eye_position[1] + 1
        percent = 50
        while True:
            if left_side > -1:
                initial_row[left_side] = percent
                left_side -= 1
            
            if right_side < len(initial_row):
                initial_row[right_side] = percent
                right_side += 1
                
            percent /= 2
            percent = int(percent)
            
            if percent < 25:
                break
        screen[eye_position[0]] = initial_row
        
        i = 0
        for pixel in screen[eye_position[0]]:
            if pixel != 10:
                n_value = int(pixel/2) if pixel > 50 else pixel
                up_ind = eye_position[0]-1
                down_ind = eye_position[0]+1
                count = 0
                while count < 2:
                    if up_ind > -1:
                        screen[up_ind][i] = n_value
                    if down_ind < 20:
                        screen[down_ind][i] = n_value
                    
                    if n_value > 25:
                        n_value = int(n_value/2)
                    up_ind -= 1
                    down_ind += 1
                    count += 1
            i += 1                    

        for x in range(len(screen)):
            n_list = ' '.join(list(map(str, screen[x])))
            screen[x] = n_list

        print('\n'.join(screen))

if __name__ == '__main__':
    main()