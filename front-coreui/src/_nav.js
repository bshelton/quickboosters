export default {
  items: [
    {
      name: 'Dashboard',
      url: '/dashboard',
      icon: 'icon-speedometer',
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
      title: true,
      name: 'Admin',
      wrapper: {
        element: '',
        attributes: {},
      },
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
    },

  ],
};
