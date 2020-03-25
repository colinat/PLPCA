## intent:greet
- hi again
- hello
- Hi
- Hello
- Hey
- hey there
- hey
- hi

## intent:goodbye
- farewell
- good bye
- see ya
- bye bye
- good night
- gotta go
- see you around
- goodnight
- bye

## intent:thanks
- thanks
- Thanks for that
- Thank you so much
- Thanks
- thnaks

## intent:ask_what_can_u_do
- help
- How can you help me?
- What can you do
- what do u do?
- help me
- what can u do

## intent:inform
- [op_costs](aspect_type)
- [op_risks](aspect_type)
- [competition](aspect_type)
- [debt](aspect_type)
- [acquisitions](aspect_type)
- [organic_expansion](aspect_type)
- [products_services](aspect_type)

## intent:query_sentiment
- How is the company's balance sheet and [debt](aspect_type) level?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- Have interest rate trends benefited/acted against the company?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- What is the [outlook](sent_polarity) for share price of the company?
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- What is the overall [outlook](sent_polarity) for the company as a whole?
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- How far can [stock price](aspect_type:earnings) go this year?
- How are company's [expenses](aspect_type:op_costs) trending?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?
- How is the company performing vs our [competitors](aspect_type:competition)?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- Will growth rate be expected to reaccelerate from here?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- Does the CEO feel [optimistic](emot_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- How have our [acquisitions](aspect_type) performed?
- Are there risks to current [profit margin](aspect_type:earnings) from any upcoming expenses?
- How should we see any impacts on [revenue](aspect_type:sales)?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- Is management [optimistic](emot_polarity)?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- Can we expect to see accelerating return from the investments?
- Is company expected to be active on the merger and acquistion front this year?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?
- So should we expect a reversal or a benefit in the fourth quarter?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- How is the broad [sentiment](sent_polarity) of management with regards to company growth?
- Is there expectation for growth to moderate?
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- Is the company [liquidity](aspect_type:debt) situation healthy?

## intent:query_sentence
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- What are the impacts on [gross margins](aspect_type:op_costs)?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?
- What caused margin [to decline](sent_polarity:negative)?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- Why have [sales](aspect_type) not been up to expectations?
- Any changes in the [sales](aspect_type) trends?
- Should we expect to see a net impact in margin?
- What is holding back the [sales](aspect_type) growth this quarter?

## intent:out_of_scope
- Where am I?
- cr
- Can I get a hamburger?
- Can you give me your datacenter's password
- are u facebook
- are you vegan
- Is this Goal-Oriented Chatbot?
- a tamed mouse will arrive at your doorstep in the next couple of days
- Have we met before?
- Order me a pizza
- are you dev?
- Can you please send me an uber
- I wan to buy a plane
- I am User
- Why is my TRUST score set to 50 after I completed the registration process?
- What did you eat yesterday?
- Is today saturday?
- Can you call me back ?
- The Try it out is not working
- I am trying to build one, and did some research before, but I have not do hand-on work yet
- I want to order pizza
- Nice name
- What's do YouTube do
- I ned a GP in 94301
- book a ticket
- I am hungry
- can you understand ?
- Recharge
- I want a new laptop
- But you're an english site :(
- Who are your customers
- can you book dinner
- alexa, order 5 tons of natrium chloride
- chinese ok?
- I am an opioid addict
- I want book a hotel
- Who’s the US President?
- call me father
- I have installed it
- chgfhgh
- What is 2 + 2?
- NLW
- buy groceries
- Can you make sandwiches?
- Can you give me your datacenter's password?
- Where am I right now?
- I need to eat cake
- 4 + 2 = ?
- can you help me with the docs?
- are you human ?
- and make chicken noises into the phone
- can you cheer me up
- What is todays date
- Won't you ask me how I am?
- aRE YOU SINGLE
- Mail me the guide
- SEL ME SOMETHING
- What day is it today?
- How long does it take to set up a Rasa bot?
- are u, facebook?
- common, just try
- are you using Rasa Core and NLU ?
- Find nearest pizzahut
- Do I have to accept?
- can you speak about politic ?
- I wanna marry you
- cannot see
- Why don’t you answer?
- Kristin, I want to marry you
- are you sick
- Pizza bot
- What's your backend system?
- can you help me with your docs
- Try it out broken
- I can barely see this white text on light gray background ...
- I'm a shitmuncher
- I want pizza
- can you cook dinner
- Today
- Are you ready?
- are the newsletter worth the subscription?
- I want french cuisine
- colder
- Can YouTube talk?
- I want to use pipe
- What is your hobbies?
- but I just told you that :(
- Do you know Kevin Pelton
- I changed my mind
- Now?
- Can I die
- I am asking you an out of scope question
- You'r blue.
- I need a job
- What do you prefer?
- can you help me with your docs?

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
