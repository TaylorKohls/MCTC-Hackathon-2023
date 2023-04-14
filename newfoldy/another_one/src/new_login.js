import {Link} from "react-router-dom"
import Button from '@mui/material/Button';

export default function LoginPage() {
    return (
        <div class="form-body">
        <div class="row">
            <div class="form-holder">
                <div class="form-content">
                    <div class="form-items">
                        <h3>Bank name</h3>
                        <p>Log in </p>
                        <form class="requires-validation" novalidate>

                            <div class="col-md-12">
                               <input class="form-control" type="text" name="name" placeholder="Full Name" required />
                               <div class="invalid-feedback">Username field cannot be blank!</div>
                            </div>

                            <div class="col-md-12">
                                <input class="form-control" type="email" name="email" placeholder="E-mail Address" required>
                                </input>
                                 <div class="invalid-feedback">Email field cannot be blank</div>
                            </div>

                           <div class="col-md-12">
                           <div class="invalid-feedback">Please select an account</div>

                                <select class="form-select mt-3" required>
                                      <option selected disabled value="">Account</option>
                                      <option value="jweb">Checking</option>
                                      <option value="sweb">Savings</option>
                                      <option value="pmanager">Credit and Loans</option>
                               </select>
                                <div class="valid-feedback">Login</div>
                           </div>


                           <div class="col-md-12">
                              <input class="form-control" type="password" name="password" placeholder="Password" required>
                              </input>

                               <div class="invalid-feedback"></div>
                           </div>


                           <div class="col-md-12 mt-3">
                            <label class="mb-3 mr-1" for="gender">Please Select a Role: </label>

                            <input type="radio" class="btn-check" name="gender" id="male" autocomplete="off" required />
                            <label class="btn btn-sm btn-outline-secondary" for="male">Existing</label>

                            <input type="radio" class="btn-check" name="gender" id="female" autocomplete="off" required />
                            <label class="btn btn-sm btn-outline-secondary" for="female">New</label>

                            {/* <input type="radio" class="btn-check" name="gender" id="secret" autocomplete="off" required />
                            <label class="btn btn-sm btn-outline-secondary" for="secret">Secret</label> */}
                            </div>

                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" value="" id="invalidCheck" required />

                          <label class="form-check-label">I confirm that all data are correct</label>
                        </div>
                  

                            <div class="form-button mt-3" >
                             <Button size="small" href="/piechart">Sign In</Button>

                                {/* <button id="submit" type="submit" class="btn btn-primary">Register   </button> */}
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    )
}