## intent:greet
- Hi
- hi again
- hey

## intent:goodbye
- see you around
- good night
- bye bye
- gotta go

## intent:thanks
- thanks
- Thanks for that

## intent:ask_what_can_u_do
- help me
- How can you help me?
- what can u do

## intent:inform
- [debt](aspect_type)
- [acquisitions](aspect_type)
- [op_costs](aspect_type)

## intent:query_sentiment
- Is there expectation for growth to moderate?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- Can we expect to see accelerating return from the investments?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- How does CEO [feel](emot_polarity) about overall [performance](aspect_type:earnings) this year?
- What is the overall [outlook](sent_polarity) for the company as a whole?
- Have interest rate trends benefited/acted against the company?
- So should we expect a reversal or a benefit in the fourth quarter?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- Is management [optimistic](emot_polarity:confident) about maintaining and expanding [margins](aspect_type:earnings)?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- How is the company planning to pay down the [debt](aspect_type) on its balance sheet?
- What is the [outlook](sent_polarity) for share price of the company?
- Will growth rate be expected to reaccelerate from here?

## intent:query_sentence
- How is the company planning to reduce [overheads](aspect_type:op_costs) in the near term?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- Any changes in the [sales](aspect_type) trends?
- Why have [sales](aspect_type) not been up to expectations?

## intent:out_of_scope
- 4 + 2 = ?
- can you cheer me up
- Can you make sandwiches?
- Can I get a hamburger?
- Is this Goal-Oriented Chatbot?
- are you sick
- can you help me with your docs
- can you help me with the docs?
- Can you give me your datacenter's password?
- Today
- are the newsletter worth the subscription?
- Is today saturday?
- are you human ?
- Who’s the US President?
- but I just told you that :(
- Do I have to accept?
- What's do YouTube do
- But you're an english site :(
- Why is my TRUST score set to 50 after I completed the registration process?
- chinese ok?
- Why don’t you answer?
- How long does it take to set up a Rasa bot?
- are you dev?
- call me father
- You'r blue.
- cr
- are u facebook
- Can I die
- Do you know Kevin Pelton
- Mail me the guide
- I ned a GP in 94301
- alexa, order 5 tons of natrium chloride
- Kristin, I want to marry you
- Pizza bot
- Now?
- are u, facebook?

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
