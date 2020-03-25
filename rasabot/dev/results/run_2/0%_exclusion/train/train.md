## intent:greet
- Hi
- hello
- hey there
- hey
- Hello
- Hey
- good evening
- good morning

## intent:goodbye
- see ya
- good night
- cya
- gotta go
- farewell
- goodbye
- bye bye
- see you around
- goodnight

## intent:thanks
- Thank you
- Thank u
- thnaks
- Thanks for that
- Thank you so much

## intent:ask_what_can_u_do
- How can you help me?
- help
- What can you do?
- What can you do
- help me
- How are you able to help me

## intent:inform
- [products_services](aspect_type)
- [op_risks](aspect_type)
- [debt](aspect_type)
- [organic_expansion](aspect_type)
- [earnings](aspect_type)
- [acquisitions](aspect_type)
- [op_costs](aspect_type)

## intent:query_sentiment
- What is the overall [outlook](sent_polarity) for the company as a whole?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- What is the [outlook](sent_polarity) for share price of the company?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- So should we expect a reversal or a benefit in the fourth quarter?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- Should we expect to see a net impact in [sales](aspect_type)?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- How is the company performing vs our [competitors](aspect_type:competition)?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- How is the company's balance sheet and [debt](aspect_type) level?
- Will I [make money](sent_polarity) from this stock this year?
- How are company's [expenses](aspect_type:op_costs) trending?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- How far can [stock price](aspect_type:earnings) go this year?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- Is the global shutdown or protests in the city likely to be [detrimental](sent_polarity) to the operations of the company
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- Would the CEO expect the [negative](sent_polarity) trend to reverse?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown
- Is CEO [optimistic](emot_polarity) about 2020 for the company
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- Is company expected to be active on the merger and acquistion front this year?
- Is the company [liquidity](aspect_type:debt) situation healthy?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- Is management [optimistic](emot_polarity)?
- How is the broad [sentiment](sent_polarity) of management with regards to company growth?
- Does the CEO feel [optimistic](emot_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- Are there risks to current [profit margin](aspect_type:earnings) from any upcoming expenses?
- Will growth rate be expected to reaccelerate from here?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's [feel](emot_polarity) towards them?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?

## intent:query_sentence
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?
- What are the impacts on [gross margins](aspect_type:op_costs)?
- What is holding back the [sales](aspect_type) growth this quarter?
- Why have [sales](aspect_type) not been up to expectations?
- What's driving the more optimistic expectation for [sales](aspect_type)?
- Are [earnings](aspect_type) performing in line with expectations?
- What are the primary drivers of [sales](aspect_type)?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- Should we expect to see a net impact in margin?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?

## intent:out_of_scope
- can you help me with the docs?
- Can I die
- are you sick
- Can I get a hamburger?
- NLW
- buy one please
- chinese ok?
- Can you give me your datacenter's password?
- Make me a sandwich
- What is your hobbies?
- Try it out broken
- I need to eat cake
- I need a GP in 94301
- common, just try
- Recharge
- can you cook dinner
- are u facebook
- call me father
- can you speak about politic ?
- are you single?
- I want to order food
- are the newsletter worth the subscription?
- can you learn from our conversation?
- Do you know Kevin Pelton
- and make chicken noises into the phone
- can you cheer me up
- cannot see
- I can barely see this white text on light gray background ...
- What's your backend system?
- I wan to buy a plane
- a tamed mouse will arrive at your doorstep in the next couple of days
- book a ticket
- Won't you ask me how I am?
- buy groceries
- are u, facebook?
- Where am I?
- Mail me the guide
- What's 1 + 1?
- again?
- I ned a GP in 94301
- You'r blue.
- Where am I right now?
- are you vegan
- I want pizza
- I wanna marry you
- connect to alexa
- are you dev?
- can you book dinner
- I want to use pipe
- Do I have to accept?
- can you give me a cup of coffee
- What's do YouTube do
- Why is my TRUST score set to 50 after I completed the registration process?
- After registration I see that I have an available balance of 0.00000000. What does this balance represent?
- Find nearest pizzahut
- german?
- cr
- What is todays date
- Are you ready?
- SEL ME SOMETHING
- but I just told you that :(
- I want a new laptop
- I changed my mind
- I want to die
- I am an opioid addic
- What did you eat yesterday?
- Who ?
- I want to order pizza
- HomeBase is advertised as a community. Is there a way to interact with other members of the community?
- Can you make sandwiches?
- but if rasa is open source why do you have a sales team
- I am trying to build one, and did some research before, but I have not do hand-on work yet
- I already told you! I'm a shitmuncher
- What is 2 + 2?
- are you russian?
- chgfhgh
- are you using Rasa Core and NLU ?
- What day is it today?
- Why don’t you answer?
- I want book a hotel
- I need a job
- Have we met before?
- Can I ask you questions first?
- I am an opioid addict
- Pizza bot
- Can YouTube talk?
- Nice name
- I have installed it
- Kristin, I want to marry you
- I am asking you an out of scope question
- Can you call me back ?
- Who are your customers
- I am User
- What do you prefer?
- The Try it out is not working
- I need a girl friend!

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
