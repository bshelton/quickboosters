export default {
  items: [
    {
      name: 'Dashboard',
      url: '/dashboard',
      icon: 'icon-speedometer',
      badge: {
        variant: 'info',
        text: 'NEW',
      },
    },
    {
      title: true,
      name: 'Profile',
      wrapper: {            // optional wrapper object
        element: '',        // required valid HTML5 element tag
        attributes: {}        // optional valid JS object with JS API naming ex: { className: "my-class", style: { fontFamily: "Verdana" }, id: "my-id"}
      },
      class: ''             // optional class names space delimited list for title item ex: "text-center"
    },
    {
      name: 'Profile',
      url: '/profile',
      icon: 'icon-drop',
    },
    {
      name: 'My Games',
      url: '/my-games',
      icon: 'icon-pencil',
    },
    {
      title: true,
      name: 'Orders',
      wrapper: {
        element: '',
        attributes: {},
      },
    },
    {
      name: 'Orders',
      url: '/orders',
      icon: 'icon-puzzle',
      children: [
        {
          name: 'My Orders',
          url: '/orders',
          icon: 'icon-puzzle',
        },
        {
          name: 'Add order',
          url: '/add-order',
          icon: 'icon-puzzle',
        },

      ],
    },
    {
      name: 'Admin',
      url: '/admin',
      icon: 'icon-cursor',
      children: [
        {
          name: 'Search',
          url: '/admin-search',
          icon: 'icon-cursor',
        },
        {
          name: 'Applications',
          url: '/applications',
          icon: 'icon-cursor',
        },
      ],
    },
    {
      name: 'Charts',
      url: '/charts',
      icon: 'icon-pie-chart',
    },
    {
      name: 'Widgets',
      url: '/widgets',
      icon: 'icon-calculator',
      badge: {
        variant: 'info',
        text: 'NEW',
      },
    },
    {
      divider: true,
    },
    {
      title: true,
      name: 'Extras',
    },
    {
      name: 'Pages',
      url: '/pages',
      icon: 'icon-star',
      children: [
        {
          name: 'Login',
          url: '/login',
          icon: 'icon-star',
        },
        {
          name: 'Register',
          url: '/register',
          icon: 'icon-star',
        },
        {
          name: 'Error 404',
          url: '/404',
          icon: 'icon-star',
        },
        {
          name: 'Error 500',
          url: '/500',
          icon: 'icon-star',
        },
      ],
    },
    {
      name: 'Disabled',
      url: '/dashboard',
      icon: 'icon-ban',
      attributes: { disabled: true },
    },
    {
      name: 'Download CoreUI',
      url: 'https://coreui.io/react/',
      icon: 'icon-cloud-download',
      class: 'mt-auto',
      variant: 'success',
      attributes: { target: '_blank', rel: "noopener" },
    },
    {
      name: 'Try CoreUI PRO',
      url: 'https://coreui.io/pro/react/',
      icon: 'icon-layers',
      variant: 'danger',
      attributes: { target: '_blank', rel: "noopener" },
    },
  ],
};
