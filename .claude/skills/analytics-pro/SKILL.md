---
description: "Expert-level analytics for Google Analytics, Facebook Analytics, YouTube Analytics, and more. Analyze like a pro: identify leaks, optimize conversions, understand customer behavior. From raw data to actionable insights."
keywords:
  - analytics
  - google analytics
  - facebook analytics
  - youtube analytics
  - data analysis
  - conversion optimization
  - user behavior
  - funnel analysis
  - cohort analysis
  - attribution
  - insights
  - reporting
---

# Analytics Pro Skill

## Purpose

Transform raw analytics data into **strategic insights**. 

This skill is for analysts who speak data fluently:
- Find the leaks in funnels
- Identify optimization opportunities
- Understand customer behavior patterns
- Track what matters (not vanity metrics)
- Make decisions based on data, not gut

**2026 Reality:**
- 80% of companies collect data but don't analyze it
- Companies using advanced analytics grow 3x faster
- Data-driven decisions beat gut calls 70% of the time
- Average funnel has 40-60% unidentified leaks
- Attribution modeling prevents $100K+ in wasted ad spend

---

## Analytics Framework: 5 Layers

```
LAYER 1: DATA COLLECTION
├─ Events tracked correctly
├─ Parameters captured
└─ Attribution model set

LAYER 2: BASELINE METRICS
├─ Traffic sources
├─ Conversion rates
├─ Retention curves
└─ Revenue metrics

LAYER 3: FUNNEL ANALYSIS
├─ Drop-off identification
├─ Stage-by-stage performance
├─ Bottleneck detection
└─ Leak quantification

LAYER 4: COHORT ANALYSIS
├─ Behavior by acquisition source
├─ User segmentation
├─ Lifetime value by cohort
└─ Churn patterns

LAYER 5: OPTIMIZATION
├─ Test results analysis
├─ Lift quantification
├─ Learning documentation
└─ Next test recommendations
```

---

## Google Analytics 4 (GA4) Expert Setup

### The Right Events to Track

**Essential Events (Must-have):**

```
E-Commerce Sites:
├─ view_item_list (browsing category)
├─ view_item (looking at product)
├─ add_to_cart (adding to cart)
├─ begin_checkout (starting checkout)
├─ add_payment_info (adding payment)
└─ purchase (completed transaction)

SaaS Sites:
├─ sign_up (account creation)
├─ begin_trial (trial starts)
├─ add_subscription (paid plan)
├─ subscription_renew (renewal)
└─ subscription_cancel (churn)

Content/Lead Sites:
├─ view_content (article/page view)
├─ view_post_engagement (time on page >30s)
├─ generate_lead (form submitted)
├─ contact (contact us filled)
└─ download (lead magnet grabbed)

B2B/Complex:
├─ join_webinar (webinar signup)
├─ attend_webinar (showed up)
├─ schedule_demo (demo booked)
├─ complete_demo (attended demo)
└─ conversion (became customer)
```

**Key Parameters to Capture:**

```
ALWAYS include:
├─ item_id (specific product/page)
├─ item_category (category/type)
├─ value (revenue if applicable)
├─ currency (USD, EUR, etc)
├─ user_segment (free/paid/premium)
└─ traffic_source (organic/paid/direct)

FOR LEAD MAGNET:
├─ magnet_type (quiz/ebook/webinar)
├─ magnet_quality (hot/warm/cold lead)
└─ conversion_stage (awareness/consideration)

FOR PERFORMANCE:
├─ experiment_id (A/B test ID)
├─ variant (control/variant_a/variant_b)
└─ expected_lift (expected improvement %)
```

---

## Facebook Analytics Expert Setup

### Events to Track (Facebook Pixel)

**Funnel Events (Priority Order):**

```
TOP PRIORITY:
1. PageView (all pages)
2. ViewContent (product/offer page)
3. Search (search on site)
4. AddToCart (e-commerce)
5. Purchase (conversion)

SECONDARY:
6. Contact (contact form)
7. CompleteRegistration (signup)
8. Lead (lead form)
9. AddPaymentInfo (payment step)

OPTIONAL (Advanced):
10. InitiateCheckout (checkout start)
11. Subscribe (subscription)
12. FindLocation (store locator)
13. Schedule (appointment)
```

### Conversion API (Server-Side Tracking)

**Better than Pixel because:**
- ✅ No iOS tracking restrictions
- ✅ More reliable (not blocked by ad blocker)
- ✅ More granular data
- ✅ Better attribution

**Setup:**
```
On purchase/signup/lead:
├─ Send event to Facebook server-side
├─ Include: customer_id, event_value, currency
├─ Include: customer_data (email, phone for matching)
└─ Include: custom_data (custom metrics)

Result: Facebook knows exact ROI of every ad
```

---

## YouTube Analytics Deep Dive

### Metrics That Matter (Not Vanity)

**Don't Focus On:**
```
❌ Total Views (meaningless, includes accidental clicks)
❌ Subscribers (if they don't watch)
❌ Comments (10 commenters ≠ 10K viewers)
```

**FOCUS ON:**

```
ENGAGEMENT:
✅ Average View Duration (AVD)
   - Your metric: How many seconds watched?
   - Industry baseline: 40-60% of video length
   - Your target: 70%+ of video length
   
✅ Click-Through Rate (CTR)
   - Your metric: % of impressions that clicked
   - Industry baseline: 3-5%
   - Your target: 8%+ (hook working)

RETENTION:
✅ Retention Curve (% still watching at each second)
   - 0-3 sec: Should be 100% (hook)
   - 50%: Where you're losing half
   - End: Final % who finished
   - Target: <20% drop in first 3 sec, then stable

DISCOVERY:
✅ Click-Through Rate (CTR) to your channel
   - Shows if thumbnail works
   - Target: 8%+

✅ Traffic Sources
   - Recommended (algorithm): How discoverable
   - Subscriptions: Loyal audience
   - Search: Long-term organic reach
```

### YouTube Analytics Data You Need

**Weekly Dashboard:**

```
For [Last 7 Days]:
├─ Total Views
├─ Average View Duration (%)
├─ Click-Through Rate (%)
├─ Watch Time Hours
├─ Subscriber Growth
├─ Traffic Sources Breakdown
├─ Audience Retention Curve
└─ Top Referring Websites (if applicable)

For [Last 30 Days]:
├─ Trending videos (which 3 performed best)
├─ Worst performers (which 3 underperformed)
├─ Subscriber quality (how many watched full video)
└─ Suggestions (what to double down on)
```

---

## Funnel Analysis: Finding Leaks

### The Leak Detection Process

**Step 1: Map Your Funnel**

```
Example E-Commerce:
Stage 1: Product Page View          10,000 users
Stage 2: Add to Cart                 2,000 users (80% drop)
Stage 3: Begin Checkout              1,500 users (25% drop)
Stage 4: Complete Checkout           1,000 users (33% drop)
Stage 5: Purchase Confirmed            800 users (20% drop)

Overall Conversion: 800/10,000 = 8% ✓ (good)
```

**Step 2: Identify Biggest Leak**

```
Drop from Stage 1 → 2: 80% (BIGGEST LEAK)
Drop from Stage 2 → 3: 25%
Drop from Stage 3 → 4: 33% (SECOND BIGGEST)
Drop from Stage 4 → 5: 20%

FIX PRIORITY:
1. First → Add to Cart (80% drop)
2. Checkout → Payment (33% drop)
3. Payment → Confirm (20% drop)
```

**Step 3: Root Cause Analysis**

```
For each leak, ask:
├─ Technical issue? (Check error logs)
├─ Friction issue? (Too many steps?)
├─ Trust issue? (No social proof? Bad reviews?)
├─ Price issue? (Unexpected fee revealed?)
├─ Clarity issue? (They don't understand value?)
└─ Intent issue? (Wrong audience, not truly interested?)
```

**Step 4: Hypothesize & Test**

```
Leak: 80% don't add to cart
Hypothesis: Product page lacks social proof
Test: Add 5 customer testimonials + rating badges
Expected Lift: 10-15% increase in add-to-cart rate
```

---

## Cohort Analysis: Behavior by Source

### Why Cohort Analysis Matters

**Without:** "Our conversion rate is 5%"  
**With:** "Organic search converts at 8%, paid ads at 3%, direct at 6%"

Same data, but NOW you see what's working.

### Cohort Analysis Template

```
COHORT: Acquisition Source × Month

           Jan    Feb    Mar    Apr    May   Trend
Organic    8%     8.2%   8.5%   8.7%   9.0%  📈 Improving
Paid Ads   3%     3.1%   2.9%   3.2%   3.0%  ⟷ Flat
Direct     6%     6.2%   5.9%   6.1%   6.3%  ↗ Stable
Referral   5%     5.5%   5.8%   6.2%   6.5%  📈 Improving

INSIGHTS:
- Organic is strongest + improving
- Paid ads underperforming, needs optimization or kill
- Referral growing (word-of-mouth effect?)
- Direct flat (need to build brand awareness)
```

### Lifetime Value (LTV) by Cohort

```
Cohort         CAC    LTV    LTV:CAC   Action
───────────────────────────────────────────────
Organic        $20    $500   25:1 ✅   SCALE
Paid Ads       $50    $350   7:1  ⚠️   Optimize
Direct         $5     $400   80:1 🚀   Invest
Referral       $0     $480   ∞    🎉   Encourage

DECISION:
- Scale organic (best ROI, improving)
- Kill paid ads (poor ROI, not improving)
- Invest in direct (best LTV, cheap CAC)
- Create referral program (highest potential)
```

---

## Retention: The Real Metric

### Retention Curve (Week-over-Week)

```
Week 1: 100% (just signed up)
Week 2: 60%  (40% churn)
Week 3: 40%  (33% of remaining churned)
Week 4: 30%  (25% of remaining churned)
Week 8: 25%  (stabilized - core users)

Good benchmark:
├─ Week 2: 40-50% retention
├─ Week 4: 25-35% retention
├─ Month 3: 15-25% retention
└─ Month 6: 10-15% retention (stabilized)

Your goal: Push that curve UP
```

### Cohort Retention Analysis

```
Cohort      W2    W4    M3    M6    M12   Assessment
─────────────────────────────────────────────────────
Jan Users   50%   35%   25%   20%   15%   Normal
Feb Users   52%   38%   28%   22%   17%   Better (?)
Mar Users   48%   33%   22%   18%   12%   Worse (?)

INSIGHT: Feb cohort has better retention
Question: What was different in Feb? (Product update? Better onboarding?)
Action: Document what worked, apply to future cohorts
```

---

## Attribution Modeling: Where Credit Goes?

### The Problem

Customer journey:
```
Day 1: See Facebook ad → No click
Day 3: Google search → Click website
Day 5: Email newsletter → Click
Day 7: Direct visit → Purchase

Who gets credit? Facebook? Google? Email? All?
```

### Attribution Models (Choose One)

```
1. FIRST-TOUCH
   Credit: Facebook (first touch)
   When to use: Awareness optimization
   
2. LAST-TOUCH (Default)
   Credit: Direct (last before purchase)
   When to use: Conversion optimization
   Problem: Undervalues top-of-funnel
   
3. LINEAR (Equal)
   Credit: Facebook 25%, Google 25%, Email 25%, Direct 25%
   When to use: Balanced view
   
4. TIME-DECAY
   Credit: Direct 40%, Email 30%, Google 20%, Facebook 10%
   Recent touches get more credit
   When to use: Most realistic (proven to work)
   
5. DATA-DRIVEN (ML-based)
   Google Analytics calculates based on your actual conversions
   Best: Most accurate, but needs 1000+ monthly conversions
```

**Recommendation:** Use TIME-DECAY or DATA-DRIVEN for accuracy.

---

## Quality Checklist

**After analyzing:**

- [ ] **Data is clean** (no duplicates, correct event capture)
- [ ] **Attribution model chosen** (and documented)
- [ ] **Funnel leaks identified** (biggest 3 quantified)
- [ ] **Root causes diagnosed** (not just symptoms)
- [ ] **Cohort analysis completed** (what's working?)
- [ ] **Retention curve analyzed** (churn pattern visible?)
- [ ] **Benchmarks set** (what's good?)
- [ ] **Tests recommended** (specific, with expected lift)
- [ ] **Next actions clear** (no ambiguity)

---

## Common Mistakes (Don't Do These)

### ❌ Mistake 1: Obsessing Over Vanity Metrics

```
❌ "We got 10,000 page views!"
✅ "10,000 page views, 2% scroll depth, 0.5% conversion"

The second tells you the truth: High traffic, low quality.
```

### ❌ Mistake 2: Ignoring Cohorts

```
❌ "Conversion rate is 5%"
✅ "Organic 8%, Paid 3%, Direct 6%"

Same data, but now you know which channel to double down on.
```

### ❌ Mistake 3: Not Tracking Retention

```
❌ "We got 1,000 new customers this month!"
✅ "We got 1,000 new customers, but 60% churned by week 2"

High growth + high churn = Leaky bucket (unsustainable).
```

### ❌ Mistake 4: Wrong Attribution Model

```
❌ Using last-touch only (undervalues ads)
✅ Using time-decay (values entire customer journey)

Difference: Wrong decisions about ad spending.
```

---

## Success Metrics

**Your analytics are working if:**

- **Clarity:** You can explain the funnel in 2 minutes
- **Action:** Every metric leads to a decision
- **Improvement:** You're testing and winning consistently
- **Team alignment:** Everyone reads the same dashboard
- **Profitability:** You understand true CAC and LTV by channel

---

## Output

When analyzing, provide:

1. **Data Quality Assessment** (is the data clean/trustworthy?)
2. **Baseline Metrics** (current state snapshot)
3. **Funnel Analysis** (biggest leaks identified + quantified)
4. **Root Cause Diagnosis** (why are the leaks happening?)
5. **Cohort Breakdown** (what's working, what isn't?)
6. **Retention Curves** (churn patterns + healthy benchmarks)
7. **Attribution Model** (recommended + why)
8. **Top 3 Opportunities** (highest impact tests to run)
9. **Expected Impact** (if you fix these 3, conversion → X%)
10. **Dashboard Template** (what to monitor weekly)

---

## Tools & Setup

**Google Analytics 4:**
- Event tracking setup (complete list)
- Conversion setup (goals)
- Audience segmentation
- Custom reports

**Facebook Analytics:**
- Pixel setup (correct events)
- Conversion API setup (server-side)
- Cohort analysis
- Retention cohorts

**YouTube Analytics:**
- Retention curve analysis
- Traffic sources breakdown
- Audience demographics
- Seasonal trends

**Dashboard Tools:**
- Google Data Studio (free, powerful)
- Tableau (professional)
- Looker (enterprise)
- Custom dashboards

---

## Sources & Frameworks

- [Google Analytics 4 Academy](https://analytics.google.com/analytics/academy/)
- [Facebook Analytics Best Practices](https://www.facebook.com/analytics/)
- [YouTube Analytics Guide](https://www.youtube.com/intitle:analytics)
- [Cohort Analysis Fundamentals](https://mixpanel.com/blog/cohort-analysis/)
- [Attribution Modeling 2026](https://www.analytics.google.com/analytics/web/)
