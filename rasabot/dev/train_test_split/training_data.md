## intent:greet
- good evening
- Hi
- hi again
- Hello
- hello
- hey there
- hey
- good morning

## intent:goodbye
- good night
- see ya
- goodnight
- bye bye
- farewell
- see you later
- goodbye
- see you around
- good bye

## intent:thanks
- Thank you so much
- Thanks for that
- Thanks
- Thank u
- thanks

## intent:ask_what_can_u_do
- How are you able to help me
- How can you help me?
- help me
- what can u do
- what do u do?
- What can you do?

## intent:inform
- [op_costs](aspect_type)
- [competition](aspect_type)
- [products_services](aspect_type)
- [op_risks](aspect_type)
- [earnings](aspect_type)
- [organic_expansion](aspect_type)
- [acquisitions](aspect_type)

## intent:query_sentiment
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- How is the company's balance sheet and [debt](aspect_type) level?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- How is the company performing vs our [competitors](aspect_type:competition)?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- What is the [outlook](sent_polarity) for share price of the company?
- Will growth rate be expected to reaccelerate from here?
- Should we expect to see a net impact in [sales](aspect_type)?
- Does the CEO feel [optimistic](emot_polarity:confident) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?
- Will I [make money](sent_polarity) from this stock this year?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- Can we expect to see accelerating return from the investments?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- What is the general [tone](emot_polarity) of management?
- How is the broad [sentiment](sent_polarity) of management with regards to company growth?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- Would the CEO expect the [negative](sent_polarity) trend to reverse?
- Are there risks to current [profit margin](aspect_type:earnings) from any upcoming expenses?
- So should we expect a reversal or a benefit in the fourth quarter?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- Will there be any new upcoming new [products](aspect_type:products_services) or services launches that we can look forward to?
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- Is the company [liquidity](aspect_type:debt) situation healthy?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- Is company expected to be active on the merger and acquistion front this year?
- How are company's [expenses](aspect_type:op_costs) trending?
- How should we see any impacts on [revenue](aspect_type:sales)?
- Is CEO [optimistic](emot_polarity:confident) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- How have our [acquisitions](aspect_type) performed?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- What is the overall [outlook](sent_polarity) for the company as a whole?

## intent:query_sentence
- What are important areas CEO highlighted about our key [competitors](aspect_type:competition)?
- Can you explain why CEO is [bearish](emot_polarity:negative) on [sales](aspect_type) and outlook of the company?
- What are the impacts on [gross margins](aspect_type:op_costs)?
- What are the primary drivers of [sales](aspect_type)?
- What has been the biggest [unexpected](sent_polarity:negative) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?
- Any explanation for the [exciting](sent_polarity:positive) outlook?
- What caused margin [to decline](sent_polarity:negative)?
- What is holding back the [sales](aspect_type) growth this quarter?
- Why is it that management is [bullish](emot_polarity:confident) on [earnings](aspect_type)?
- What are some driving factors behind managements [positive opinion](sent_polarity:positive) on [earnings](aspect_type)?
- Why is sentiment for [operating costs](aspect_type:op_costs) so [negative](sent_polarity)?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- What are the reasons behind the forecast for [rising costs](sent_polarity:negative)?
- What's driving the more [optimistic](emot_polarity) expectation for [sales](aspect_type)?
- What is CEO's thoughts on our [competitors](aspect_type:competition)?
- Can you elaborate on the reasons behind management's [optimism](emot_polarity:confident)?
- What did CEO say about upcoming [earnings](aspect_type) forecast?
- Why have [sales](aspect_type) not been up to expectations?
- What are factors influencing [gross margin](aspect_type:op_costs)?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- What is driving the increase in [costs](aspect_type:op_costs)/[favourable](sent_polarity:positive) drop in costs?
- Any comments on possible [acquisitions](aspect_type)?
- Any outlook on where our biggest [costs](aspect_type:op_costs) are going to trend?
- What are key things management highlighted about our [borrowings](aspect_type:debt) and [interest costs](aspect_type:debt)?
- Why is outlook for [earnings](aspect_type) so [bad](sent_polarity:negative)?
- Are [earnings](aspect_type) performing in line with expectations?
- Can you tell me why CEO is so [upbeat](sent_polarity:positive) on upcoming performance?
- Any changes in the [sales](aspect_type) trends?

## intent:out_of_scope
- But you're an english site :(
- Recharge
- I want french cuisine
- I need a GP in 94301
- but if rasa is open source why do you have a sales team
- SEL ME SOMETHING
- What's your backend system?
- can you help me with your docs
- Can you give me your datacenter's password
- I ned a GP in 94301
- I changed my mind
- I am trying to build one, and did some research before, but I have not do hand-on work yet
- I need a girl friend!
- Have we met before?
- Do I have to accept?
- I'm stuffing
- Pizza bot
- Can you give me your datacenter's password?
- colder
- I want book a hotel
- can you cheer me up
- You'r blue.
- are you human ?
- I want pizza
- I already told you! I'm a shitmuncher
- Where am I?
- are you sick
- What makes you better than a human?
- Who’s the US President?
- I need to eat cake
- I want to order pizza
- chgfhgh
- are the newsletter worth the subscription?
- Order me a pizza
- can you cook dinner
- alexa, order 5 tons of natrium chloride
- chinese ok?
- Today
- Do you know Kevin Pelton
- What do you prefer?
- are u facebook
- can you help me with the docs?
- I want to use pipe
- can you give me a cup of coffee
- Why don’t you answer?
- What's do YouTube do
- I am an opioid addict
- Can I die
- common, just try
- book a ticket
- german?
- The weather is good
- Why is my TRUST score set to 50 after I completed the registration process?
- a tamed mouse will arrive at your doorstep in the next couple of days
- I have installed it
- again?
- can you book dinner
- NLW
- What day is it today?
- Can I ask you questions first?
- Mail me the guide
- are you using Rasa Core and NLU ?
- can we keep chatting?
- buy groceries
- buy one please
- I wan to buy a plane
- I am User
- Is today saturday?
- I am an opioid addic
- connect to alexa
- I'm a shitmuncher
- are you vegan
- Is this Goal-Oriented Chatbot?
- Can I get a hamburger?
- What's 1 + 1?
- are you russian?
- Find nearest pizzahut
- Won't you ask me how I am?
- I want a new laptop
- Can you call me back ?
- Nice name
- I am asking you an out of scope question
- Kristin, I want to marry you
- Make me a sandwich
- Where am I right now?
- The Try it out is not working
- Try it out broken
- call me father
- What is your hobbies?
- What did you eat yesterday?
- are you single?
- Who ?
- is the ceo hungry?
- Can you make sandwiches?
- I wanna marry you
- cannot see
- I want to die
- What is 2 + 2?

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a human?

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
- bullish
- optimism

## synonym:debt
- gearing
- leverage
- geared
- liquidity
- financing
- borrowings
- interest costs
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
- unexpected
- rising costs
- bearish
- bad
- poor

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
- market share
- expansion
- expansion plans
- growth strategy

## synonym:positive
- favourable
- upbeat
- exciting
- positive opinion

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
