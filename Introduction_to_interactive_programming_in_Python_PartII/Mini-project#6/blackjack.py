# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
#score = 0
player_score = 0
dealer_score = 0
player_hand = []
dealer_hand = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        ans = ''
        for cards in self.hand:
            ans = ans + str(cards) + ' '
        
        return 'Hand contains ' + ans

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        ace = False

        for card in self.hand:
            rank = card.get_rank()
            value += VALUES[rank]

            if rank == 'A':
                ace = True

        if value < 11 and ace:
            value += 10

        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 80
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop(0)
    
    def __str__(self):
        # return a string representing the deck
        ans = ''
        for cards in self.cards:
            ans = ans + str(cards) + ' '
        
        return 'Deck contains ' + ans



#define event handlers for buttons
def deal():
    global outcome, in_play, message, player_hand, dealer_hand, deck, dealer_score, player_score
    
    if in_play:
        outcome = "Player lost because of re-deal!. New deal?"
        dealer_score += 1
        in_play = False
    
    else: # initialize the Deck and Shuffle
        deck = Deck()
        outcome = 'Welcome to a new Game!'
        deck.shuffle()

    # Create the player and dealer hands
        player_hand = Hand()
        dealer_hand = Hand()
    
    # Add two cards to each hand    
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        
        message = "Hit or Stand?"
    
        in_play = True

def hit():
    global outcome, in_play, dealer_score, message
    # if the hand is in play, hit the player
    
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
   
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have busted. New deal?"
            in_play = False
            dealer_score += 1
            message = ''

def stand():
    global outcome, player_score, dealer_score, in_play, message
    
    in_play = False
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
    
    # assign a message to outcome, update in_play and score
    
    if dealer_hand.get_value() > 21:
        outcome = "Dealer busted. Congratulations!"
        player_score += 1
        message = 'New Deal?'
        
    else:
        if dealer_hand.get_value() >= player_hand.get_value() or player_hand.get_value() > 21:
            outcome = "Dealer wins. New deal?"
            dealer_score += 1
            message = ''
        else:
            outcome = "Player wins. New deal?"
            player_score += 1
            message = ''
    

    

# draw handler    
def draw(canvas):
    global outcome, in_play, card_back, player_score, dealer_score, message

    canvas.draw_text("Blackjack", [220, 50], 50 ,"Lime")

    player_hand.draw(canvas, [100, 300])
    dealer_hand.draw(canvas, [100, 150])

    canvas.draw_text(outcome, [10, 100], 30 ,"Lime")
    canvas.draw_text(message, [200,480], 26, "Black")

    canvas.draw_text("Dealer: %s" % dealer_score, [10, 150], 20 ,"Black")
    canvas.draw_text("Player: %s" % player_score, [10, 300], 20 ,"White")

    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,199), CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric