## intent:greet
- Hello
- hello
- Hey

## intent:goodbye
- farewell
- see ya
- see you around
- cya

## intent:thanks
- Thank you so much
- thnaks

## intent:ask_what_can_u_do
- How can you help me?
- help
- What can you do

## intent:inform
- [products_services](aspect_type)
- [debt](aspect_type)
- [op_risks](aspect_type)

## intent:query_sentiment
- Is company expected to be active on the merger and acquistion front this year?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- Is the company [liquidity](aspect_type:debt) situation healthy?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- How is the company performing vs our [competitors](aspect_type:competition)?
- How are company's [expenses](aspect_type:op_costs) trending?
- Is management [optimistic](emot_polarity)?
- What is the [outlook](sent_polarity) for share price of the company?
- Will I [make money](sent_polarity) from this stock this year?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?

## intent:query_sentence
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?
- What is holding back the [sales](aspect_type) growth this quarter?
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- Will the guidance of 5% be higher than what the company has done throughout the course of this year?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?

## intent:out_of_scope
- Won't you ask me how I am?
- are the newsletter worth the subscription?
- I wanna marry you
- I need to eat cake
- Have we met before?
- What is todays date
- Why don’t you answer?
- I want to order food
- Can you give me your datacenter's password?
- I am an opioid addict
- I want to use pipe
- buy one please
- Recharge
- Where am I?
- can you help me with the docs?
- chinese ok?
- I wan to buy a plane
- are u facebook
- I am asking you an out of scope question
- I can barely see this white text on light gray background ...
- Do you know Kevin Pelton
- connect to alexa
- can you give me a cup of coffee
- a tamed mouse will arrive at your doorstep in the next couple of days
- can you cook dinner
- are you single?
- I need a job
- Can I ask you questions first?
- book a ticket
- Nice name
- chgfhgh
- buy groceries
- I am an opioid addic
- cr
- Why is my TRUST score set to 50 after I completed the registration process?
- can you learn from our conversation?

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
