import { AppBar, Button, Typography, Toolbar } from "@mui/material";
import React from "react";
import LoginIcon from "@mui/icons-material/Login";
import LogoutIcon from "@mui/icons-material/Logout";

export default function Navbar() {
  return (
    <AppBar position="fixed">
      <Toolbar>
        <Typography variant="h5" flexGrow={1}>
          Crypto Currency Live Prediction
        </Typography>
        <Button variant="text" color="inherit" startIcon={<LoginIcon />}>
          Login
        </Button>
        <Button variant="text" color="inherit" endIcon={<LogoutIcon />}>
          Logout
        </Button>
      </Toolbar>
    </AppBar>
  );
}
