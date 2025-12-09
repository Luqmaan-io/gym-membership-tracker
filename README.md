# Gym Membership Tracker

## About 
This application is intended to be used by owners and staff of gyms in order to keep up to date with their members and their memberships to those gyms as well as storing key contact information needed for communication or emergencies.

This is a gym management platform designed to provide a reliable backend architecture for handling essential gym operations such as membership tracking, payment records, and attendance logging. The focus of this project is on functionality, maintainability, and data structure, creating a scalable foundation that can be expanded with additional features in the future.
---

## Features

### Implemented Features
- ✅ **Member Management**: Add, view, edit, and delete gym members
- ✅ **Membership Plans**: Create different membership tiers with pricing
- ✅ **Authentication**: Gym owner login/logout with session management
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile
- ✅ **CRUD Operations**: Full Create, Read, Update, Delete functionality

### Future Features
- 🔄 Payment tracking and invoicing
- 🔄 Attendance logging with check-in system
- 🔄 Reports and analytics dashboard
- 🔄 Inventory management for supplements


## UX Design

### User Stories 

As a Gym Owner, I want to add new members with their contact and emergency information so that I can grow my member base safely and maintain proper records.  

As a Gym Owner, I want to assign members to different membership plans with start and expiry dates so that I can manage different pricing tiers and automate renewals.  

As a Staff Member, I want to search for and view a member's full profile so that I can quickly access their contact details and emergency information when needed.  

As a Staff Member, I want to log a member's check-in so that I can track attendance and know who is currently in the gym.  

As a Staff Member, I want to record a payment against a member's account so that I can keep their membership active and track revenue.


## Entity Relationship Diagram (ERD)

The following diagram represents the database structure for the Gym Membership Tracker.  
It illustrates how the main entities — GymOwner, Member, MembershipPlan, Payment, and Attendance — relate to each other.

- Each **GymOwner** can have multiple **Members**.  
- Each **Member** belongs to one **GymOwner** and one **MembershipPlan**.  
- Each **Member** can have multiple **Payments** and **Attendance** records.

![ERD Diagram](assets/wireframes/erd.png)

---
### Stratergy  
The main users of this platform are the owners and staff of gyms. Users can view and manage gym members, update their membership details, and handle payment records. The system aims to reduce manual paperwork and make gym administration more efficient and data-driven.

This platform helps gym owners track key business information, such as member activity, payment status, and plan types all from one place.

Gym owners have reported experiencing the following issues with software they're currently using:

- Many customers still pay in cash, but their systems are designed only for card payments, resulting in separate handwritten records.

- Their systems lack flexibility for tracking temporary freezes or adjustments to memberships.

- Inventory tracking (e.g., for drinks or supplements) is inconsistent, with no easy way to monitor stock levels.

The main goal of this project is to help gym owners manage their businesses with greater efficiency and accuracy, providing a system that proactively assists with daily operations rather than reacting to problems.

---

### Scope
This system is a "back-office" management software designed specifically for gym owners and staff. The core purpose is to streamline daily operations and provide clear visibility of membership and payment data.

#### Core Membership & Operations

- Dashboard: Overview of key metrics (active members, today’s revenue, total memberships).  
- Member Management: Add, edit, and view member profiles including contact and emergency information.  
- Payment Records: Record and view payments, track amounts due, and identify overdue members.  
- Membership Plans: Assign members to plans (e.g., monthly, annual) with start and expiry dates.  
- Attendance Tracking: Log and monitor member check-ins.  

#### Business Insights

- Membership Statistics: Overview of how many members are active, inactive, or frozen.  
- Revenue Tracking: Breakdown of income from memberships and other payments.  

#### Future Developments

- Inventory Management: Track sales and stock of supplements or merchandise.  
- Referral System: Allow members to refer friends and earn rewards.  
- Guest Pass System: Manage guest entries and conversions to full members.  
- Predictive Insights: Identify at-risk members or forecast stock needs.  
- QR/Barcode Check-In: Optional feature for quick access at the front desk.  
---

### Structure
The following will show different user flows when using the system.  

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

---