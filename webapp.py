from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('question.html')
    
@app.route("/home")
def render_home(): 
    user = request.args['uname']
    trophy_count = request.args.get('trophy_count', 'Not specified')
    messages = {
        "Have not played": "Welcome to Brawl Stars Recommendations! Since you're a new player that has never played Brawl Stars before, I'm just going to explain what it is. Brawl Stars is a competitive multiplayer game released by Supercell where you can play as several different characters and fight other people. There are many different modes and the game is regularly updated. Winning a game gets you trophies, and it is basically the ranking system in the game.",
        "0-15000": "Welcome to Brawl Stars Recommendations! You've really only just jumped down the rabbit hole, and you might be here for a while. At this trophy range, I'd suggest getting a lot of brawlers up to power level 7 or 9. It's the easiest to push without being severely expensive in terms of coins or power points, and as long as you have some skill at the game, it shouldn't be too difficult to push up to rank 20. If you ever have any issues with coins, a very quick way to get them is through masteries, which you unlock by winning with brawlers. It gives 750-1000 coins on the first mastery rank-up, which you can usually unlock around rank 15.",
        "15001-30000": "Welcome to Brawl Stars Recommendations! You probably know how to play the game at this point, but I'm still going to give a couple of things that I'd like to suggest. At this trophy range and above, you should definitely have most of your brawlers leveled up to around 7-9. Whenever you unlock a new brawler, it's always nice to level them up and push them to a somewhat high trophy range, since it gives a free break and free trophies. It's also really good to find a club or friend group that plays the game a lot at this range, since here and below, you might have a tough time finding good teammates.",
        "30001-50000": "Welcome to Brawl Stars Recommendations! At this trophy range, there's not too much to recommend. Find a brawler that you think you're good at, hard push them as high as possible until you start to lose a couple of games. At this point, you should start maxing out the level of your brawlers, since at this trophy range, your opponents will be good at the game.",
        "50001+": "Welcome to Brawl Stars Recommendations! You likely know how to play already, and there's really not that much I can recommend that someone of this range wouldn't know already. Just keep doing what you're doing, since you're having a lot of success already."
    }
    specific_message = messages.get(trophy_count, "No specific recommendations available.")
    return render_template('home.html', response1=specific_message, username=user)

@app.route("/redirect")
def redirect_to_realterms():
    user = request.args.get('uname')  # ai gen 
    return render_template('realterms.html', uname=user)
    
@app.route("/verif")
def render_verif(): 
    return render_template('verify.html')
    
if __name__=="__main__":
    app.run(debug=True)

