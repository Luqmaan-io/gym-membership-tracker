# Gym Membership Tracker

## About 
This application is intended to be used by owners and staff of gyms in order to keep up to date with their members and their memberships to those gyms as well as storing key contact information needed for communication or emergencies.  

This is a full scale gym management platform that focuses on providing a robust and scalable backend architecture for handling membership tracking, payment records, and attendance logging.

## UX Design

### Stratergy  
The main users of this platform are to be the owners of gyms as well as their staff. Users are able to track memberships of gym goers allowing staff to make neccesary updates to details of members, updating / suspending / cancelling / freezing their memberships. The platform would aim to help gym owners operate their gyms from a better business angle, providing crucial data on number of active memebrships, their monthly incomings from membership plans, sale of products and merchandise as well as helping keep on top of stock levels.  

Gym owners have reported experiencing the following issues with software they're currently using:  

- A lot of the guys pay in cash, the system is built for card payments so they end up keeping a separate cash log in a notebook.  
- Guest pass system too generic. They want to track who brought them in and if that person signs-up, to then thank the member with a free protein shake or preworkout drink etc.  
- Inventory system is an afterthought, no pre-warning that they're low on stock 

The main goal with this project is to help gym owners manage their businesses with more efficiency by creating a system that is more proactive rather than reactive.


### Scope
This system is a "back-office" management software designed specifically for gym owners and staff. The core purpose is to streamline daily operations and to provide deep business insights.  

Features to be developed:  
Core memebership & operations
- Dashboard: At a glance view of key meetrics (days's revenue, low stock alerts)
- Member management: profile view, QR code check-in
- Payment processing  
- Referal systemop0

Business insights:
- Suuplement profitability
- Membership plan performance
- Predictive insights (at-risk member flagging, resource / inventory forecasting)

### Structure
The following will show different user flows when using the system.  

---

1. Daily Member Check-In (Front Desk Staff)  

Goal: Get a member from the door to the gym floor in under 10 seconds.  
START: Staff member is on the main "Dashboard" screen.  
ACTION: Staff clicks the large "Check-In" button on the dashboard, or scans a member's key tag/card using a barcode scanner.  
SYSTEM RESPONSE: The system automatically opens the check-in window with the scanner input focused. If scan/search is successful: The member's profile picture, name, and membership status ("Active") instantly appear.
If membership is expired/frozen: A clear warning message appears (e.g., "Membership Paused - Please See Manager").

ACTION: Staff sees the green "Active" status and clicks the "Check In" button.

SYSTEM RESPONSE: A success message ("Welcome, John!") flashes on screen.
The system logs the check-in timestamp and closes the window.  
The dashboard's "Active Members Now" counter increments by one.

END: Staff is back on the dashboard, ready for the next member.  

---
2. Managing a "Soft" Membership Freeze (Gym Owner/Manager)  

Goal: Pause a loyal member's membership for a non-standard period without hassle.  
START: From the dashboard, the owner searches for and opens the member's profile (e.g., "Mike").  
ACTION: On Mike's profile page, the owner clicks the "Freeze Membership" button.  
SYSTEM RESPONSE: A simple modal/pop-up appears with two fields:  
Reason (Dropdown: Injury, Vacation, Off-Season, Other)  
Duration (Two options: Standard Policy OR Custom: [ ] Days)

ACTION: Owner selects "Off-Season" and types 21 in the "Custom Days" field.  
ACTION: Owner clicks "Apply Freeze".

SYSTEM RESPONSE: The system calculates the auto-resume date (e.g., "Will auto-resume on Nov 25"). Mike's status on his profile updates to "Frozen (Until Nov 25)". The system creates a calendar entry to auto-resume billing.  

END: Owner closes Mike's profile. The task is complete with no manual reminders needed.

---
3. Processing a Cash Payment & Logging a Supplement Sale (Front Desk Staff)

Goal: Log a financial transaction and update inventory in one seamless flow.  
START: Staff is in the member's profile page (e.g., "Sarah").  
ACTION: Staff clicks the "Take Payment" button.  
SYSTEM RESPONSE: The "Process Payment" screen opens, defaulting to Sarah's monthly membership fee.

ACTION: Staff changes Payment Method to "Cash". Staff clicks "Add Item" and selects "Pre-Workout (Scoop)" from the inventory list.

SYSTEM RESPONSE: The system adds the scoop to the transaction and shows a running total.  

ACTION: Staff clicks "Process Payment & Print Receipt".

SYSTEM RESPONSE: The system records the cash payment against Sarah's account. It decrements the "Pre-Workout" inventory by one serving.
It sends the receipt to the connected printer.  

END: Staff hands the receipt to Sarah. The dashboard's "Today's Revenue" updates.

### Skeleton
---
### Surface

1. Design Philosophy & Mood
Keywords: Power, Clarity, Durability, Focus.

Inspiration: Industrial gym aesthetics—brushed metal, rubber mats, dark tones with bold accent colours. The interface should feel like a gym enivronment.

Goal: Reduce visual noise. Prioritise data and actions. Make the system enjoyable to use for long, stressful shifts.

---
2. Colour Palette
Primary Background: #1a1a1a (Near black). Reduces eye strain in low-light environments and makes content pop.  
Secondary Background/Cards: #2d2d2d (Dark grey). Used for card surfaces and modals.

Primary Accent: #f5a623 (Amber/Orange). A high-energy, warning colour used for primary buttons and key interactive elements. It feels strong, not playful.  
Secondary Accent: #4a90e2 (Cool Blue). Used for informational links, secondary actions, and positive financial data.

Status Colours:  
Success: #7ed321 (Green)  
Warning: #f5a623 (Amber)  
Error/Danger: #d0021b (Red)

Text:  
Primary Text: #ffffff (White)  
Secondary Text: #b3b3b3 (Light Grey)

---
3. Typography
Font Family: Inter or Roboto. Sans-serif, highly legible, and professional. No serifs, no decorative fonts.

Hierarchy:  
H1 (Page Title): 28px, Semi-Bold, White. e.g., "Dashboard"  
H2 (Section Headers): 20px, Semi-Bold, White. e.g., "At-Risk Members"

Body Text: 16px, Regular, White.  
Secondary Text / Labels: 14px, Regular, #b3b3b3.  
Button Text: 16px, Medium, White.

---
4. Imagery & Icons
Icons: Heroicons or Feather Icons. Outline style for a clean, modern feel. Consistent stroke width.  
Member Photos: Circular thumbnails. If no photo is provided, a default silhouette icon is used against a gradient background.