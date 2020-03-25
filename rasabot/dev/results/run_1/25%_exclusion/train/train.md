## intent:greet
- hey
- Hey
- hi again
- hi
- hello
- Hi

## intent:goodbye
- see you around
- gotta go
- good night
- see ya
- bye bye
- farewell
- goodnight

## intent:thanks
- Thanks for that
- Thank you so much
- thanks
- Thanks

## intent:ask_what_can_u_do
- What can you do
- How can you help me?
- what can u do
- help me
- what do u do?

## intent:inform
- [competition](aspect_type)
- [acquisitions](aspect_type)
- [op_costs](aspect_type)
- [op_risks](aspect_type)
- [products_services](aspect_type)
- [debt](aspect_type)

## intent:query_sentiment
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- Does the CEO feel [optimistic](emot_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- What is the [outlook](sent_polarity) for share price of the company?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- Have interest rate trends benefited/acted against the company?
- Will growth rate be expected to reaccelerate from here?
- What is the CEO's [feel](emot_polarity) about the new [challengers](aspect_type:competition) in the industry?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- Is management [optimistic](emot_polarity)?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- Is the company [liquidity](aspect_type:debt) situation healthy?
- Is there expectation for growth to moderate?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- What is CEO's [outlook](sent_polarity) on the [debt](aspect_type) refinancing situation of the company
- How is the broad [sentiment](sent_polarity) of management with regards to company growth?
- What is the overall [outlook](sent_polarity) for the company as a whole?
- How is the company's balance sheet and [debt](aspect_type) level?
- So should we expect a reversal or a benefit in the fourth quarter?
- Is management [confident](emot_polarity) of beating street expectations for earnings this year?
- Cost-income ratio seems to be trending up what does management [feel](emot_polarity) about this trend in the coming year?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- How far can [stock price](aspect_type:earnings) go this year?
- Is company expected to be active on the merger and acquistion front this year?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- Can we expect to see accelerating return from the investments?

## intent:query_sentence
- Which are some of the [rising costs](sent_polarity:negative) that management foresee will hit the company's [bottom line](aspect_type:earnings) this year?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?
- Should we expect to see a net impact in margin?
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- Why have [sales](aspect_type) not been up to expectations?
- What are the impacts on [gross margins](aspect_type:op_costs)?
- Any changes in the [sales](aspect_type) trends?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?

## intent:out_of_scope
- But you're an english site :(
- Can you call me back ?
- can you cheer me up
- can you book dinner
- are u facebook
- can you help me with your docs
- Are you ready?
- Can YouTube talk?
- What is todays date
- SEL ME SOMETHING
- How long does it take to set up a Rasa bot?
- Why don’t you answer?
- I am hungry
- What is your hobbies?
- I am trying to build one, and did some research before, but I have not do hand-on work yet
- Pizza bot
- Can I get a hamburger?
- I wan to buy a plane
- Is this Goal-Oriented Chatbot?
- Recharge
- What's do YouTube do
- aRE YOU SINGLE
- I can barely see this white text on light gray background ...
- 4 + 2 = ?
- Now?
- buy groceries
- Can I die
- are you using Rasa Core and NLU ?
- I am User
- Why is my TRUST score set to 50 after I completed the registration process?
- Who are your customers
- are you sick
- but I just told you that :(
- I am an opioid addict
- I need a job
- Kristin, I want to marry you
- Can you give me your datacenter's password?
- I'm a shitmuncher
- What is 2 + 2?
- I ned a GP in 94301
- can you cook dinner
- I wanna marry you
- are the newsletter worth the subscription?
- and make chicken noises into the phone
- chinese ok?
- Do I have to accept?
- can you understand ?
- Do you know Kevin Pelton
- Order me a pizza
- I want book a hotel
- are u, facebook?
- can you speak about politic ?
- Can you give me your datacenter's password
- alexa, order 5 tons of natrium chloride
- cr
- What do you prefer?
- Can you make sandwiches?
- are you dev?
- NLW
- Today
- What day is it today?
- call me father
- Who’s the US President?
- Is today saturday?
- colder
- are you human ?
- I have installed it
- You'r blue.
- Mail me the guide
- can you help me with the docs?
- I want a new laptop
- Where am I?

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
