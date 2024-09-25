---
aliases: 
theme: 
high_priority: false
tags:
---
**

Coding With Brian, Project Bank PostgreSQL Tables:

  
```sql

For the Users:

CREATE TABLE "Users" (

  id SERIAL PRIMARY KEY,

  name VARCHAR(255) NOT NULL,

  email VARCHAR(255) NOT NULL UNIQUE,

  password VARCHAR(255) NOT NULL,

  role VARCHAR(255) CHECK (role IN ('admin', 'lender', 'borrower')) DEFAULT 'borrower' NOT NULL,

  "isActive" BOOLEAN DEFAULT TRUE,

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()

);

  

For the Transactions: 

CREATE TABLE "Transactions" (

  reference VARCHAR(255) NOT NULL UNIQUE,

  email VARCHAR(255) NOT NULL,

  amount INTEGER NOT NULL,

  status VARCHAR(255) NOT NULL,

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()

);

  

For the Support Request:

CREATE TABLE "SupportRequests" (

  id SERIAL PRIMARY KEY,

  "userId" INTEGER NOT NULL,

  message TEXT NOT NULL,

  status VARCHAR(255) CHECK (status IN ('Pending', 'In Progress', 'Resolved')) DEFAULT 'Pending',

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  FOREIGN KEY ("userId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  

For the Settings

CREATE TABLE settings (

  "interestRate" FLOAT NOT NULL,

  "repaymentTerm" INTEGER NOT NULL,

  fees FLOAT NOT NULL,

  "termsOfService" TEXT,

  "privacyPolicy" TEXT

);

  

For the Loans

CREATE TABLE "Loans" (

  amount FLOAT NOT NULL,

  "interestRate" FLOAT NOT NULL,

  term INTEGER NOT NULL,

  purpose VARCHAR(255) NOT NULL,

  status VARCHAR(255) DEFAULT 'pending',

  "borrowerId" INTEGER NOT NULL,

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()

);

  
  

Repayments table:

CREATE TABLE "Repayments" (

  id SERIAL PRIMARY KEY,

  "loanId" INTEGER NOT NULL,

  "lenderId" INTEGER NOT NULL,

  "borrowerName" VARCHAR(255) NOT NULL,

  amount FLOAT NOT NULL,

  "repaymentDate" DATE NOT NULL,

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  FOREIGN KEY ("loanId") REFERENCES "Loans" (id) ON DELETE CASCADE,

  FOREIGN KEY ("lenderId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
  

Notifications Table:

CREATE TABLE "Notifications" (

  id SERIAL PRIMARY KEY,

  "lenderId" INTEGER NOT NULL,

  title VARCHAR(255) NOT NULL,

  message TEXT NOT NULL,

  type VARCHAR(255) NOT NULL, -- e.g., 'loan_status', 'repayment_update', 'announcement'

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  FOREIGN KEY ("lenderId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
  
  
  

Loan Report Table:

CREATE TABLE "LoanReports" (

  "totalLoans" INTEGER NOT NULL,

  "totalFunds" FLOAT NOT NULL,

  "totalRepayments" FLOAT NOT NULL,

  "activeLoans" INTEGER NOT NULL,

  "overdueLoans" INTEGER NOT NULL,

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()

);

  
  

Loans table:

CREATE TABLE "Loans" (

  "id" SERIAL PRIMARY KEY,

  "borrowerId" INTEGER NOT NULL,

  "borrowerName" VARCHAR(255) NOT NULL,

  "amount" DECIMAL(10, 2) NOT NULL,

  "term" INTEGER NOT NULL,

  "interestRate" DECIMAL(5, 2) NOT NULL,

  "purpose" VARCHAR(255) NOT NULL,                -- Added purpose field

  "repaymentSchedule" VARCHAR(255) NOT NULL,      -- Added repaymentSchedule field

  "riskLevel" VARCHAR(255) NOT NULL,

  "repaymentAmount" FLOAT,                        -- Added repaymentAmount field

  "status" ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',

  "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

  FOREIGN KEY ("borrowerId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
  

Lender Profile Table:

CREATE TABLE "LenderProfiles" (

    "id" SERIAL PRIMARY KEY,

    "userId" INTEGER NOT NULL UNIQUE,

    "firstName" VARCHAR(255) NOT NULL,

    "lastName" VARCHAR(255) NOT NULL,

    "phone" VARCHAR(255),              -- Optional phone field

    "address" VARCHAR(255),            -- Optional address field

    "bio" TEXT,                        -- Optional bio field

    "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    FOREIGN KEY ("userId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
  

Loan Lender Table:

CREATE TABLE "Loan-lender" (

    "id" SERIAL PRIMARY KEY,

    "amount" FLOAT NOT NULL,

    "term" INTEGER NOT NULL,

    "interestRate" FLOAT NOT NULL,

    "borrowerId" INTEGER NOT NULL,

    "status" VARCHAR(255) DEFAULT 'Pending',  -- Options: Pending, Approved, Funded

    "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    FOREIGN KEY ("borrowerId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
  
  

Investment Table:

CREATE TABLE "Investment" (

    "id" SERIAL PRIMARY KEY,

    "amount" FLOAT NOT NULL,

    "lenderId" INTEGER NOT NULL,

    "loanId" INTEGER NOT NULL,

    "status" VARCHAR(255) DEFAULT 'pending',  -- Options: pending, funded

    "repaymentProgress" FLOAT DEFAULT 0,

    "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    FOREIGN KEY ("lenderId") REFERENCES "Users" (id) ON DELETE CASCADE,

    FOREIGN KEY ("loanId") REFERENCES "Loan-lender" (id) ON DELETE CASCADE

);

  
  

Borrower Repayment Table:

CREATE TABLE "borrower-Repayment" (

    "id" SERIAL PRIMARY KEY,

    "amount" FLOAT NOT NULL CHECK ("amount" > 0), -- Ensure the amount is positive

    "date" TIMESTAMP WITH TIME ZONE NOT NULL,

    "loanId" INTEGER,

    "borrowerId" INTEGER,

    "createdAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    "updatedAt" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    FOREIGN KEY ("loanId") REFERENCES "Loans" (id) ON DELETE CASCADE,

    FOREIGN KEY ("borrowerId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
  

Borrower Notification Table(We will be using this as our notification Table as compared to the previous Notification Table that I gave you previously above)

CREATE TABLE "borrowser-notification" (

    "id" SERIAL PRIMARY KEY,

    "userId" INTEGER NOT NULL,

    "message" VARCHAR NOT NULL,

    "status" VARCHAR CHECK ("status" IN ('sent', 'delivered', 'read')) DEFAULT 'sent',

    "createdAt" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    FOREIGN KEY ("userId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
  

Borrower Loan Table:

CREATE TABLE "borrower-Loan" (

    "id" SERIAL PRIMARY KEY,

    "borrowerId" INTEGER NOT NULL,

    "amount" FLOAT NOT NULL,

    "term" INTEGER NOT NULL,

    "purpose" VARCHAR NOT NULL,

    "status" VARCHAR CHECK ("status" IN ('pending', 'approved', 'rejected')) DEFAULT 'pending',

    "interestRate" FLOAT NOT NULL,

    "repaymentSchedule" JSON NOT NULL,

    "createdAt" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    "updatedAt" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    FOREIGN KEY ("borrowerId") REFERENCES "Users" (id) ON DELETE CASCADE

);

  
```
  
  
**