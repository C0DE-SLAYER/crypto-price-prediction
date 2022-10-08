import React, { Component } from 'react'
import {
  Link
} from "react-router-dom";

export default class Login extends Component {
  render() {
    return (
      <div>
        <section class="login">
          <div class="login_box">
            <div class="left">
              <div class="contact">
                <form action="">
                  <h3>SIGN IN</h3>
                  <input type="text" placeholder="First Name"/>
                  <input type="text" placeholder="Last Name"/>
                  <input type="text" placeholder="Email-id"/>
                  <input type="text" placeholder="USERNAME"/>
                    <input type="text" placeholder="PASSWORD"/>
                      <Link to="/"><button class="submit">LET'S GO</button></Link>
                    </form>
                  </div>
              </div>
              <div class="right">
                <div class="right-text">
                  <h2>Register</h2>
                  <h5>You have the ability to control the world!  </h5>
                </div>
                <div class="right-inductor"><img src="" alt=""/></div>
              </div>
            </div>
        </section>
      </div>
    )
  }
}
