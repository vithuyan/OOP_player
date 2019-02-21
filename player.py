# Create a class called Player.
# Every player should have three attributes: gold_coins, health_points, and lives.
# lives should start at 5.
# gold_coins should start at 0.
# health_points should start at 10.
# Define an __str__() instance method.
# Your class should have an instance method called level_up that increases lives by one.
# Your class should have an instance method called collect_treasure that increases gold_coins by one. If gold_coins is a multiple of ten (eg, 10, 20, 30, and so on) then the collect_treasure method should run the level_up method.
# Your class should have an instance method called do_battle that accepts one damage argument and subtracts it from the player's health_points. If health_points falls below one, subtract one from lives and reset health_points to ten. If you have run out of lives, this method should run another method called restart (see below).
# The restart instance method should set all attributes back to their starting values (5, 0, and 10).
# Don't forget to test out your code every step of the way by creating instances of your class and trying to run your different methods. You should be committing every time you get a new method working.


class Player:
    def __intit__(self, name, gold_coins = 0, health_points =10, lives = 5):
        self.name = name
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives

    def __str__(self):
        return "Player: name: {} - gold_coins: {} - health_points: {} - lives: {}.". format(self.name, self.gold_coins, self.health_points, self.lives)

    def level_up(self):
        self.lives += 1
        return self.lives

    def collect_treasure (self):
        self.gold_coins += 1
        if self.gold_coins % 10:
            return self.level_up()
        else:
            return self.gold_coins

    def do_battle (self, damage):
        if self.health_points -= 1:

           self.lives -= 1
        self.health_points = 10
        if health_points < 1:

           self.restart()

    def restart(self):
        self.__init__()           
