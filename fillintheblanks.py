def main():
    cases = int(input())

    for case in range(cases):
        data_lines, message_lines = list(map(int,input().split()))
        data = [input() for idx in range(data_lines)]
        message = [input() for idx in range(message_lines)]
        data_dict = {dt.split(': ')[0]:dt.split(': ')[1] for dt in data}
        formatted_message = []
        for line in message:
            new_line = line
            for key in data_dict.keys():
                while f'[{key}]' in new_line:
                    new_line = new_line.replace(f'[{key}]', data_dict[key])
            formatted_message.append(new_line)
        #print('\n'.join(formatted_message))
        for line in formatted_message:
            print(line)

if __name__ == '__main__':
    main()