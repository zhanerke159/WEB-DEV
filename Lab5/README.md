# Online Store (Angular)

This project is an Angular online store application built as part of Lab 5.
The application demonstrates component-based architecture, category-based
product filtering, and interactive UI features.

---

## 🚀 Features

- Category-based product hierarchy
- Exactly 4 categories with 5 products each (20 products total)
- Products are linked to real items on kaspi.kz
- Like button for each product
- Delete product with confirmation dialog
- WhatsApp and Telegram share functionality
- Responsive layout using CSS Grid
- Clean separation of components using Input / Output

---

## 🧩 Component Architecture

The application is built with **exactly three components**:

### AppComponent
- Displays list of categories
- Tracks the selected category
- Shows welcome message if no category is selected
- Passes filtered products to ProductListComponent

### ProductListComponent
- Receives products via `@Input()`
- Renders a list of ProductItemComponent
- Displays message when no products are available
- Emits delete events to the parent

### ProductItemComponent
- Displays product details (image, name, price, description)
- Like button that increments likes
- Delete button with confirmation dialog
- Share buttons (WhatsApp / Telegram)

---

## 📦 Data Models

- **Category**
  - `id: number`
  - `name: string`

- **Product**
  - `id: number`
  - `name: string`
  - `description: string`
  - `price: number`
  - `rating: number`
  - `images: string[]`
  - `link: string`
  - `categoryId: number`
  - `likes: number`

All data is stored in a service and not hardcoded inside components.

