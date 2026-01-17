import React from "react";
import { createRoot } from "react-dom/client"; // CHANGED: React 18 import
import { Provider } from "react-redux";
import { BrowserRouter } from "react-router-dom";

import { ModalProvider, Modal } from "./context/Modal.jsx";
import configureStore from "./store";
import * as sessionActions from "./store/session";
import App from "./App.jsx"; // CHANGED: Added .jsx extension

import "./index.css";

const store = configureStore();

// CHANGED: process.env -> import.meta.env
if (import.meta.env.MODE !== "production") {
  window.store = store;
  window.sessionActions = sessionActions;
}

function Root() {
  return (
    <ModalProvider>
      <Provider store={store}>
        <BrowserRouter>
          <App />
          <Modal />
        </BrowserRouter>
      </Provider>
    </ModalProvider>
  );
}

// CHANGED: New React 18 render method
const root = createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>
);
