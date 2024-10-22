## KARATU E-COMMERCE STORE

### 1.0 PRODUCT SUMMARY

<p>
Karatu is an e-commerce platform that enables users to purchase various products online and have them delivered to their preferred locations. The platform primarily sells two categories of products: electronics and grocery items. Karatu aims to provide a seamless and efficient online shopping experience with secure payment options and fast delivery. The platform supports both individual consumers and internal management users to ensure smooth operations.
</p>

### 2.0 PRODUCT REQUIREMENT

#### 1.0 PRODUCT USERS
<p>
The platform caters to two major categories of users: External Users (Customers) and Internal Users (Administrators).
</p>

### 1.1 External Users (Customers)
#### Signup and Login:
- Customers can sign up on the platform with their email or phone number.
- Sign-in options include email/username and password with or without   multi-factor authentication (MFA) for added security.

- Customers can also log in using their social media accounts like Google, Facebook, and Twitter for convenience.

#### User Profile Management:

- Customers can manage their profile by updating personal information (name, email, address, phone number, etc.).

- They can view their order history and track the status of active orders.

#### Shopping Experience:

- Customers can browse and search for products by category (electronics or groceries).

- Customers can add products to their cart, view the cart, update quantities, or remove items.

- The platform will support wishlists, allowing customers to save items for future purchases.

#### Checkout and Payment:
- Customers can proceed to checkout, where they can select from available delivery options.

- Payment methods include credit/debit cards, mobile money, PayPal, and other supported payment gateways.

#### Order Tracking:

- After placing an order, customers can view the real-time status of their order, including estimated delivery times.

#### 1.2 Internal Users (Admin, Super Admin, and Backend Users)

#### Admin Users:

- Admins have access to manage the customer accounts, view customer activity, and oversee order management.

- Admins can update product listings, including descriptions, prices, availability, and categories.

#### Super Admin Users:

- Super admins have all the privileges of Admins but can also manage other admin users and backend settings.

- They can assign and manage user roles, set privileges, and handle critical platform configurations.

#### Ordinary Users (Staff):

- Ordinary staff users can assist with backend operations like processing customer orders, managing inventory, and providing customer support.

#### Service Management:

- Internal users will manage key services like delivery tracking, payment confirmation, and communication with delivery partners.

#### 2.0 MAJOR SERVICES

<p>
The platform offers several core services to both customers and administrators:
</p>

#### 1. Product and Inventory Management:

- Internal users can add, remove, or update product listings in the system.

- The system tracks stock levels and sends alerts when inventory needs to be replenished.

#### 2. Delivery Services:

- The platform integrates with multiple delivery partners to provide customers with different delivery options.

- Delivery status can be updated and tracked by both customers and internal users.

#### 3. Payment Services:

- Integration with payment gateways to process customer payments securely.

- Payment confirmation, refunds, and invoicing will be handled automatically.

#### 4. Customer Support:

- Customers can open support tickets for order issues, refunds, or general queries.

- Support staff can manage customer queries, and admins can oversee all communications.

### 3.0 API DESIGN

<p>
The platform's APIs will allow external applications and frontend clients to interact with Karatu’s backend. The API will follow RESTful principles and use JSON for data interchange.
</p>

### Authentication APIs

#### POST /signup

- Registers a new customer.
- Input: {}
- Output: {}

#### POST /Login

- Logs in the customer or admin based on credentials.
- Input:{ }
- Output: { }

#### POST /social-login

- Logs in users via social accounts like Google, Facebook, or Twitter.

- Input: { }
- Output: { }

#### POST /mfa/enable

- Enables MFA for the user.
- Input: { }
- Output: { }

#### Product and Order APIs

#### GET /products

- Retrieves a list of available products.
- Input: { }
- Output: { }

#### POST /cart/add

- Adds a product to the customer's cart.
- Input: { }
- Output: { }

#### POST /checkout

- Proceeds to payment and places an order.
- Input: { }
- Output: { }

#### GET /orders/{order_id}

- Retrieves the details of a specific order

### Admin and User Management APIs

#### GET /admin/users

- Retrieves a list of all users for admins.

#### POST /admin/users/{user_id}/disable

- Disables a customer or admin account.

#### POST /admin/products/add

- Adds a new product to the platform.
- Input: {  }
- Output: { }

### Delivery and Payment APIs

#### POST /payment
- Processes the payment and returns a payment confirmation.

- Input: {  }

- Output: { }

### POST /delivery/track
- Tracks the current status of a delivery.

- Input: {  }

- Output: { }









