## intent:greet
- Hey
- hi

## intent:goodbye
- see ya
- bye bye
- farewell

## intent:thanks
- thanks
- thnaks

## intent:ask_what_can_u_do
- help
- How can you help me?

## intent:inform
- [competition](aspect_type)
- [op_risks](aspect_type)

## intent:query_sentiment
- How are cashflows of the company and can we expect more paring down of [debt](aspect_type) going forward?
- Is the company [liquidity](aspect_type:debt) situation healthy?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Are there risks to current [profit margin](aspect_type:earnings) from any upcoming expenses?
- What is the [outlook](sent_polarity) for share price of the company?
- Would the CEO expect the [negative](sent_polarity) trend to reverse?
- Interest rates are trending down are there plans to use more [debt](aspect_type) to grow the business given the low cost of financing?
- How are company's [expenses](aspect_type:op_costs) trending?
- Is company expected to be active on the merger and acquistion front this year?
- Will growth rate be expected to reaccelerate from here?

## intent:query_sentence
- What are the primary drivers of [sales](aspect_type)?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?
- What is driving the increase in [costs](aspect_type:op_costs)/favourable drop in costs?
- Should we expect to see a net impact in margin?

## intent:out_of_scope
- Can I die
- Where am I?
- I need a girl friend!
- How long does it take to set up a Rasa bot?
- I need a GP in 94301
- a tamed mouse will arrive at your doorstep in the next couple of days
- and make chicken noises into the phone
- What's 1 + 1?
- are the newsletter worth the subscription?
- are you dev?
- can you speak about politic ?
- I am an opioid addict
- Who are your customers
- The weather is good
- I need to eat cake
- can you help me with the docs?
- call me father
- can you understand ?
- Can you make sandwiches?
- Do you know Kevin Pelton
- 4 + 2 = ?
- Pizza bot
- SEL ME SOMETHING
- can you help me with your docs

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
