class Stats():
    '''остлеживание статы'''
    def __init__(self):
        '''инициализирует статы'''
        self.reset_stats()
        self.run_game = True
        with open('highscore' , 'r') as f:
            self.high_score = int(f.readline())
    def reset_stats(self):
        '''стата, изменяющаяся во время игры'''
        self.guns_left = 3
        self.score = 0