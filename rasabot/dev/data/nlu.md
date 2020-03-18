## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hi
- Hey
- Hello
- hi again

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- goodnight
- good bye
- good night
- see ya
- cya
- bye bye
- gotta go
- farewell

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thank u
- Thanks for that
- thanks
- thnaks

## intent:inform
- [sales](aspect_type)
- [earnings](aspect_type)
- [op_costs](aspect_type)
- [products_services](aspect_type)
- [organic_expansion](aspect_type)
- [acquisitions](aspect_type)
- [competition](aspect_type)
- [op_risks](aspect_type)
- [debt](aspect_type)

## intent:query_sentiment
- Should we expect to see a net impact in [sales](aspect_type)?
- Would the CEO expect the [negative](sent_polarity) trend to reverse?
- So should we expect a reversal or a benefit in the fourth quarter?
- Is there expectation for growth to moderate? 
- Will growth rate be expected to reaccelerate from here?
- Are company [operating costs](aspect_type:op_costs) under control and within expectations?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- How are company's [expenses](aspect_type_op_costs) trending?
- Is management [optimistic](sent_polarity) about maintaining and expanding [margins](aspect_type:earnings)?
- Are there risks to current [profit margin](aspect_type:earnings) from any upcoming expenses?
- Cost-income ratio seems to be trending up what does management feel about this trend in the coming year?
- Oil prices are rising would these rising [costs](aspect_type:op_costs) be a challenge for the company?
- Does the CEO feel [optimistic](sent_polarity) about the rising [costs](aspect_type:op_costs) in the company reversing trend?
- How have our [acquisitions](aspect_type) performed?
- What are plans for new [products](aspect_type:products_services) and services launches going forward?
- Can we expect to see accelerating return from the investments?
- Can we expect new product launches or [acquisitions](aspect_type) that can boost earnings in the coming financial year?
- Is company expected to be active on the merger and acquistion front this year?
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- Are earnings from [acquisitions](aspect_type) expected to grow from here?
- How is the company performing vs our [competitors](aspect_type:competition)?
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year? 
- What does management feel about the [competitive landscape](aspect_type:competition) in the near term for the company?
- What is the CEO's feel about the new [challengers](aspect_type:competition) in the industry?
- Is CEO [optimistic](sent_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- There has been some new [competitors](aspect_type:competition) on the block - What is the CEO's feel towards them?
- Can we expect heightened [risks](aspect_type:op_risks) from the economic slowdown 
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- Is the global shutdown or protests in the city likely to be detrimental to the operations of the company
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- How is the company's balance sheet and [debt](aspect_type) level?
- Have interest rate trends benefited/acted against the company?
- What does management expect [debt](aspect_type) trends for the company to be going forward?
- Does the company expect [gearing](aspect_type:debt) levels to come down going forward?
- How are cashflows of the company and can we expect more paring down of [debt](aspect_type) going forward?
- The company seem over [leverage](aspect_type:debt) are there plans to decrease our liabilities?
- The company seems too highly [geared](aspect_type:debt) would there be plans to deleverage to reduce interest costs?
- What is CEO's outlook on the [debt](aspect_type) refinancing situation of the company
- Is the company liquidity situation healthy?
- Is management expected to take on more financing to grow the business?
- Interest rates are trending down are there plans to use more debt to grow the business given the low cost of financing?
- How is the company planning to pay down the debt on its balance sheet?
- What is the general tone of management?
- Is management [optimistic](sent_polarity)?
- What is the overall outlook for the company as a whole?
- What is the outlook for share price of the company?
- How is the broad sentiment of management with regards to company growth?
- Is CEO [optimistic](sent_polarity) about 2020 for the company
- How far can [stock price](aspect_type:earnings) go this year?
- Will I make money from this stock this year?
- Is management [confident](sent_polarity) of beating street expectations for earnings this year?
- How does CEO feel about overall [performance](aspect_type:earnings) this year?
- Any effects on [performance](aspect_type:earnings) with regards to the macro environment?


## intent:query_summary
- What are the primary drivers of [sales](aspect_type)?
- Any major concerns regarding [sales](aspect_type) that investors should be aware of?

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## synonym:sales
- revenue
- sales
- net revenue
- topline

## synonym:earnings
- net profit
- bottomline
- eps
- EPS 
- result
- net margin
- net margins
- profit margin

## synonym:op_costs
- opex
- operational cost
- operation cost
- operating cost
- operating costs
- operational expense
- operation expense
- expenses

## synonym:products_services
- products
- business
- business division
- biz
- products

## synonym:organic_expansion
- expansion
- expansion plans
- growth strategy

## synonym:acquisitions
- aquisition
- acquistion
- M&A 

## synonym:competition
- competitive landscape
- competitors

## synonym:op_risks
- risks
- business risks
- operational risk
- operation risk
- operating risk
- ops risks

## synonym:debt
- leverage
- gearing









