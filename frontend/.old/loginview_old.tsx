/*import React from 'react';
import Cookies from 'universal-cookie';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { Loading } from './loading';

interface User {
  name: string;
  id: number;
  score: number;
}

type UserState = User | null;

interface LoginState {
  username: string;
  password: string;
  error: string;
  isAuthenticated: boolean;
}

interface LoginProps {
  loggedIn: boolean;
  login: (u: User) => void;
  logout: () => void;
  user: UserState;
}

interface LoginValues {
  username: string;
  password: string;
}

//const login = async (values: LoginValues) => {
//  try {
//    var resp = await fetch('/api/login/', {
//      method: 'POST',
//      headers: {
//        'Content-Type': 'application/json',
//        'X-CSRFToken': cookies.get('csrftoken'),
//      },
//      credentials: 'same-origin',
//      body: JSON.stringify(values),
//    });
//    var data = await this.isRespOk(resp);
//    console.log(data);
//    this.setState({isAuthenticated: true, username: '', password: '', error: ''});
//    this.props.setUser(data.user);
//  } catch(err) {
//    console.log(err);
//    this.setState({error: 'Wrong username or password.'});
//  }
//}
//
//async logout() {
//  try {
//    var resp = await fetch('/api/logout', {
//      credentials: 'same-origin',
//    });
//    var data = await this.isRespOk(resp);
//    console.log(data);
//    this.setState({isAuthenticated: false});
//    this.props.setUser(null);
//    this.updateAuth();
//  } catch(err) {
//    console.log(err);
//  }
//};


const FLoginView = ({ loggedIn, login, logout }: LoginProps) => {

}

const cookies = new Cookies();

export default class LoginView extends React.Component<LoginProps, LoginState> {
  constructor(props: LoginProps) {
    super(props);
    this.state = {
      username: '',
      password: '',
      error: '',
      isAuthenticated: false,
    };
  }

  componentDidMount() {
    this.getSession();
  }

  updateAuth() {
    if (this.state.isAuthenticated && !this.props.loggedIn)
      this.props.login();
    else if (!this.state.isAuthenticated && this.props.loggedIn)
      this.props.logout();
  }

  async getSession() {
    try {
      var resp = await fetch('/api/session/', { credentials: 'same-origin' });
      //var data = await resp.json();
      var data = await this.isRespOk(resp);

      console.log(data);
      this.setState({ isAuthenticated: data.isAuthenticated });
      this.updateAuth();

    } catch(err) {
      console.log(err);
    }
  }

  async whoami() {
    try {
      var resp = await fetch('/api/whoami/', {
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'same-origin',
      });
      var data = await this.isRespOk(resp);
      console.log(`Logged in as ${data.username}`)
    } catch(err) {
      console.log(err);
    }
  }

  handlePasswordChange(event: React.ChangeEvent<HTMLInputElement>) {
    this.setState({password: event.target.value});
  }

  handleUserNameChange(event: React.ChangeEvent<HTMLInputElement>) {
    this.setState({username: event.target.value});
  }

  isRespOk(response: Response) {
    if (response.status >= 200 && response.status <= 299) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  }

  async login(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    try {
      var resp = await fetch('/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': cookies.get('csrftoken'),
        },
        credentials: 'same-origin',
        body: JSON.stringify({username: this.state.username, password: this.state.password}),
      });
      var data = await this.isRespOk(resp);
      console.log(data);
      this.setState({isAuthenticated: true, username: '', password: '', error: ''});
      this.props.setUser(data.user);
      this.updateAuth();
    } catch(err) {
      console.log(err);
      this.setState({error: 'Wrong username or password.'});
    }
  }

  async logout() {
    try {
      var resp = await fetch('/api/logout', {
        credentials: 'same-origin',
      });
      var data = await this.isRespOk(resp);
      console.log(data);
      this.setState({isAuthenticated: false});
      this.props.setUser(null);
      this.updateAuth();
    } catch(err) {
      console.log(err);
    }
  };

  render() {
    //return (
    //  <>
    //  {
    //    this.state.isAuthenticated
    //      ? ''
    //      : ''
    //  }
    //  </>
    //);
    if (!this.state.isAuthenticated) {
      return (
        <div className="py-4">
          <div className="text-center">
            <h1>Create Account or Login</h1>
          </div>
          <div className="row mt-4">
            <div className="col-3 d-none d-md-block"></div>
            <div className="col-12 col-md-6">
              <LoginForm login={login} user={user}/>
            </div>
            <div className="col-3 d-none d-md-block"></div>
          </div>
        </div>
      );
      //return (
      //  <div className='container mt-3'>
      //    <h2>Login</h2>
      //    <form onSubmit={e => this.login(e)}>
      //      <div className='form-group'>
      //        <label htmlFor='username'>Username</label>
      //        <input
      //          type='text'
      //          className='form-control'
      //          id='username'
      //          name='username'
      //          value={this.state.username}
      //          onChange={e => this.handleUserNameChange(e)}
      //        />
      //      </div>
      //      <div className='form-group'>
      //        <label htmlFor='username'>Password</label>
      //        <input
      //          type='password'
      //          className='form-control'
      //          id='password'
      //          name='password'
      //          value={this.state.password}
      //          onChange={e => this.handlePasswordChange(e)}
      //        />
      //        <div>
      //          {
      //            this.state.error 
      //              &&  <small className='text-danger'>
      //                    {this.state.error}
      //                  </small>
      //          }
      //        </div>
      //      </div>
      //      <button type='submit' className='btn btn-primary'>Login</button>
      //    </form>
      //  </div>
      //);
    } else {
      return (
        <div className='container mt-3'>
          <p>You are logged in!</p>
          <button
            className='btn btn-primary mr-2'
            onClick={() => this.whoami()}
          >
            WhoAmI
          </button>
          <button
            className='btn btn-danger'
            onClick={() => this.logout()}
          >
            Log out
          </button>
        </div>
      );
    }
  }
}

const SignupSchema = Yup.object().shape({
  username: Yup.string()
    .min(2, 'Too Short!')
    .max(50, 'Too Long!')
    .required('Required'),
  password: Yup.string()
    .min(10, 'Too Short!')
    .required('Required'),
  confirmPassword: Yup.string()
    .required('Required')
    .when('password', {
      is: (val: string) => (val && val.length > 0 ? true : false),
      then: Yup.string().oneOf(
        [Yup.ref('password')],
        'Needs to match password'
      )
    }),
  email: Yup.string().email('Invalid email').required('Required'),
});

const SignupForm = () => (
  <Formik
    initialValues={{
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
    }}
    validationSchema={SignupSchema}
    onSubmit={values => {
      // same shape as initial values
      console.log(values);
    }}
  >
    {({ isSubmitting }) => (
      <Form>
        <div className='form-row'>
          <div className='form-group col-12 col-md-6'>
            <label>Username</label>
            <Field name='username' className='form-control'/>
            <ErrorMessage name='username' component='div' className='text-danger'/>
          </div>
          <div className='form-group col-12 col-md-6'>
            <label>Email</label>
            <Field type='email' name='email' className='form-control'/>
            <ErrorMessage name='email' component='div' className='text-danger'/>
          </div>
        </div>

        <div className='form-row'>
          <div className='form-group col-12 col-md-6'>
            <label>Password</label>
            <Field name='password' type='password' className='form-control'/>
            <ErrorMessage name='password' component='div' className='text-danger'/>
          </div>

          <div className='form-group col-12 col-md-6'>
            <label>Confirm Password</label>
            <Field name='confirmPassword' type='password' className='form-control'/>
            <ErrorMessage name='confirmPassword' component='div' className='text-danger'/>
          </div>
        </div>
        <button className='btn btn-primary' type='submit' disabled={isSubmitting}>Signup</button>
      </Form>
    )}
  </Formik>
);

const isRespOk = (response: Response) => {
  if (response.status >= 200 && response.status <= 299) {
    return response.json();
  } else {
    throw Error(response.statusText);
  }
}

const LoginForm = ({ login, user }: LoginProps) => (
  <Formik
    initialValues={{
      username: '',
      password: '',
    }}
    onSubmit={values => {
      console.log(values);
      (async () => {
        try {
          var resp = await fetch('/api/login/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': cookies.get('csrftoken'),
            },
            credentials: 'same-origin',
            body: JSON.stringify(values),
          });
          var data = await isRespOk(resp);
          console.log(data);
          login(data.user);
        } catch(err) {
          console.log(err);
        }
      })().then();
    }}
  >
    {({ isSubmitting }) => (
      isSubmitting
        ? <Loading message='Logging in...'/>
        : (
            user
              ? <div className="text-center">Logged in as {user.name}!</div>
              : <Form>
                  <div className='form-row'>
                    <div className='form-group col-12 col-md-6'>
                      <label>Username</label>
                      <Field name='username' className='form-control'/>
                    </div>
                  </div>
                  <div className='form-row'>
                    <div className='form-group col-12 col-md-6'>
                      <label>Password</label>
                      <Field name='password' type='password' className='form-control'/>
                    </div>
                  </div>
                  <button className='btn btn-primary' type='submit' disabled={isSubmitting}>Login</button>
                </Form>
          )
    )}
  </Formik>
  );*/
