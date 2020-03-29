## intent:greet
- Hey
- hello
- Hi
- hey there
- hi again
- Hello
- hey
- good morning

## intent:goodbye
- cya
- gotta go
- farewell
- goodbye
- see you around
- good night
- see ya
- see you later
- bye bye

## intent:thanks
- thanks
- Thank you so much
- Thanks
- Thank you
- thnaks

## intent:ask_what_can_u_do
- How are you able to help me
- help
- What can you do?
- How can you help me?
- what do u do?
- What can you do

## intent:inform
- [debt](aspect_type)
- [competition](aspect_type)
- [earnings](aspect_type)
- [op_risks](aspect_type)
- [acquisitions](aspect_type)
- [op_costs](aspect_type)
- [organic_expansion](aspect_type)

## intent:query_sentiment
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's [feel](emot_polarity) towards them?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown
- What is the general [tone](emot_polarity) of management?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- What is the overall [outlook](sent_polarity) for the company as a whole?
- How should we see any impacts on [revenue](aspect_type:sales)?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- How is the company performing vs our [competitors](aspect_type:competition)?
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- How far can [stock price](aspect_type:earnings) go this year?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- How is the company's balance sheet and [debt](aspect_type) level?
- Should we expect to see a net impact in [sales](aspect_type)?
- What is the [outlook](sent_polarity) for share price of the company?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- Is there expectation for growth to moderate?
- Does the CEO feel [optimistic](emot_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- Will growth rate be expected to reaccelerate from here?
- How have our [acquisitions](aspect_type) performed?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- How is the broad [sentiment](sent_polarity) of management with regards to company growth?
- Will I [make money](sent_polarity) from this stock this year?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- Is the company [liquidity](aspect_type:debt) situation healthy?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- How are company's [expenses](aspect_type:op_costs) trending?
- How are cashflows of the company and can we expect more paring down of [debt](aspect_type) going forward?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- So should we expect a reversal or a benefit in the fourth quarter?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?

## intent:query_sentence
- Any changes in the [sales](aspect_type) trends?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- What are the impacts on [gross margins](aspect_type:op_costs)?
- What's driving the more optimistic expectation for [sales](aspect_type)?
- Why have [sales](aspect_type) not been up to expectations?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- Are [earnings](aspect_type) performing in line with expectations?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?
- What are the primary drivers of [sales](aspect_type)?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- What are factors influencing [gross margin](aspect_type:op_costs)?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?

## intent:out_of_scope
- Can I die
- Do you know Kevin Pelton
- are you human ?
- buy groceries
- I am User
- are u facebook
- alexa, order 5 tons of natrium chloride
- but if rasa is open source why do you have a sales team
- can we keep chatting?
- I need to eat cake
- I am trying to build one, and did some research before, but I have not do hand-on work yet
- are u, facebook?
- chinese ok?
- can you understand ?
- Why don’t you answer?
- Is this Goal-Oriented Chatbot?
- I am asking you an out of scope question
- Where am I right now?
- You'r blue.
- can you help me with the docs?
- Can I get a hamburger?
- are you using Rasa Core and NLU ?
- Who are your customers
- What's your backend system?
- I have installed it
- I want book a hotel
- Make me a sandwich
- Recharge
- but I just told you that :(
- buy one please
- are you sick
- SEL ME SOMETHING
- NLW
- are the newsletter worth the subscription?
- a tamed mouse will arrive at your doorstep in the next couple of days
- Today
- I want to die
- Kristin, I want to marry you
- are you dev?
- The Try it out is not working
- aRE YOU SINGLE
- HomeBase is advertised as a community. Is there a way to interact with other members of the community?
- I need a GP in 94301
- Can you give me your datacenter's password
- Nice name
- Have we met before?
- I wanna marry you
- Where am I?
- Won't you ask me how I am?
- Can you give me your datacenter's password?
- Can YouTube talk?
- How long does it take to set up a Rasa bot?
- colder
- Is today saturday?
- I want pizza
- Can I ask you questions first?
- are you russian?
- Why is my TRUST score set to 50 after I completed the registration process?
- Who’s the US President?
- Who ?
- can you cheer me up
- I am an opioid addict
- What is 2 + 2?
- Do I have to accept?
- Mail me the guide
- What did you eat yesterday?
- are you vegan
- Are you ready?
- I want to order pizza
- I need a job
- call me father
- 4 + 2 = ?
- are you single?
- The weather is good
- Try it out broken
- I need a girl friend!
- But you're an english site :(
- book a ticket
- Can you make sandwiches?
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- can you book dinner
- german?
- I can barely see this white text on light gray background ...
- What makes you better than a human?
- chgfhgh
- I changed my mind
- I want to use pipe
- I want french cuisine
- I want to order food
- Now?
- I wan to buy a plane
- What's do YouTube do
- cr
- I already told you! I'm a shitmuncher
- can you speak about politic ?
- What do you prefer?

## intent:bot_challenge
- am I talking to a human?
- are you a bot?
- are you a human?

## synonym:acquisitions
- aquisition
- acquisituoin
- buyout
- M&A
- mergers

## synonym:competition
- competitors
- competitive landscape
- challengers

## synonym:confident
- optimistic

## synonym:debt
- gearing
- leverage
- geared
- liquidity
- financing
- loan
- loans

## synonym:earnings
- margins
- profit margin
- stock price
- performance
- bottom line
- net profit
- bottomline
- eps
- EPS
- result
- net margin
- net margins

## synonym:negative
- to decline
- rising costs

## synonym:op_costs
- operating costs
- costs
- expenses
- gross margin
- gross margins
- cost
- overheads
- opex
- operational cost
- operation cost
- operating cost
- operational expense
- operation expense

## synonym:op_risks
- risks
- challenges
- business risks
- operational risk
- operation risk
- operating risk
- ops risks

## synonym:organic_expansion
- expansion
- expansion plans
- growth strategy

## synonym:products_services
- products
- business
- business division
- biz

## synonym:sales
- revenue
- sales
- net revenue
- topline
