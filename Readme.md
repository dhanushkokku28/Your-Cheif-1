# 🍲 Smart Recipe Finder-Your Cheif

Welcome to **Smart Recipe Finder**, my final course project! This application will help users discover delicious recipes **based on the ingredients they already have at home**, reducing food waste and making cooking more fun.

Throughout this course, I will apply the topics we’ll cover — including Prompting, Retrieval-Augmented Generation (RAG), Structured Output, and Function Calling — directly in this project.

---

## 📌 Project Overview

Smart Recipe Finder is an AI-powered recipe assistant that:
- Lets users input ingredients they currently have.
- Suggests recipes that match those ingredients with minimal or no extras.
- Returns easy-to-follow steps in a structured format.
- Supports interactive features like adding missing ingredients to a shopping list or saving recipes for later.

---

## 🎯 Course Concepts and How I’ll Use Them

### ✅ Prompting
I’ll use advanced prompt engineering to interact naturally with users. For example:
> “I have rice, tomatoes, and chicken. What can I cook in under 30 minutes?”

I’ll craft prompts that guide the LLM to understand ingredient constraints, cooking time, and cuisine preferences.

---

### ✅ Retrieval-Augmented Generation (RAG)
I’ll connect the app to a **recipe database or vector store**, retrieving recipes relevant to the user’s available ingredients. The retrieved recipes will be passed to the model so it can generate personalized, accurate suggestions.

---

### ✅ Structured Output
I’ll ensure the app gets responses from the LLM in **structured JSON format**, enabling the frontend to render:
- Recipe titles
- Ingredients (with missing items highlighted)
- Step-by-step instructions
- Cooking time and calories

This structured approach will make it easy to display data consistently.

---

### ✅ Function Calling
I’ll implement function calls to:
- Fetch recipes by ingredients: `getRecipesByIngredients()`
- Add missing ingredients to a shopping list: `addToShoppingList()`
- Save recipes to favorites: `saveRecipe()`

This will enable seamless integration between user commands and backend functionality.

---

## 🛠 Planned Tech Stack

| Layer    | Tech                      |
|----------|---------------------------|
| Frontend | React / Next.js           |
| Backend  | Node.js + Express         |
| LLM      | OpenAI GPT-4 (function calling) |
| DB       | MongoDB + Pinecone/FAISS  |

---

## 📈 Planned Features

- Ingredient-based recipe suggestions
- Personalized recipe recommendations
- Shopping list management
- Save & organize favorite recipes

---
